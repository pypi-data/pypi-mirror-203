# Copyright (c) 2020-2023, Gauss Machine Learning GmbH. All rights reserved.
# This file is part of the Optimyzer API Client, which is released under the BSD 3-Clause License.

"""
This module includes the Machine class, which is used to create and access optimizations.
"""
from typing import Any, Dict, List, Optional, Tuple, Union

from .api_connection import CallType, handle_error, OptimyzerConnection
from .optimization import Optimization, Setting


class Machine:
    """
    Machines provide a useful way of clustering optimizations for knowledge transfer.
    For example, many optimizations are run on a laser cutting machine for different materials.
    Optimyzer transfers the experience from previous optimizations in a machine to each new
    optimization created.

    The variables indicate what changes between optimizations. For example, that can be the
    material type and material thickness.
    Each variable has a name and a dictionary containing its `type` and `units` (optional).
    """

    def __init__(
        self,
        uid: str,
        name: str,
        description: str,
        variables: Dict[str, Dict[str, str]],
        optimizations: List[str],
        created_on: str,
        connection: OptimyzerConnection,
    ) -> None:
        self._uid = uid
        self._name = name
        self._description = description
        self._variables = variables
        self._optimizations = optimizations
        self._created_on = created_on
        self._connection = connection
        self._optimization: Optional[Optimization] = None

    @property
    def name(self) -> str:
        """Return the machine's name"""
        return self._name

    @property
    def description(self) -> str:
        """Return the machine's description"""
        return self._description

    @property
    def created_on(self) -> str:
        """Return the date when the machine was created"""
        return self._created_on

    @property
    def variables(self) -> Dict[str, Dict[str, str]]:
        """Return the machine's variables"""
        return self._variables

    @property
    def optimization(self) -> Optimization:
        """
        Return the active optimization.
        Raises a RuntimeError is no optimization has been selected.
        """
        if self._optimization is None:
            raise RuntimeError(
                "No optimization selected! "
                "Please select a optimization using its uniqe identifier first."
            )
        return self._optimization

    @classmethod
    def from_uid(cls, uid: str, connection: OptimyzerConnection) -> "Machine":
        """
        Get a machine from the API using its unique identifier.
        """
        res = connection.call(CallType.POST, "machine/get_machine_and_opts", uid)
        if res.status_code != 200:
            handle_error(res)

        machine_dict, optimizations = res.json()
        machine_dict["uid"] = uid
        machine_dict["optimizations"] = optimizations
        for var_name, variable in machine_dict["variables"].items():
            if variable["type"] == "cat":
                values_seen = set([opt["variables"][var_name] for opt in optimizations])
                machine_dict["variables"][var_name]["values_seen"] = values_seen

        return cls(
            uid,
            machine_dict["name"],
            machine_dict["description"],
            machine_dict["variables"],
            machine_dict["optimizations"],
            machine_dict["created_on"],
            connection,
        )

    def get_all_optimizations(self) -> List[str]:
        """Return the machine's optimizations"""
        return self._optimizations

    def add_optimization(
        self,
        name: str,
        description: str,
        variables: Dict[str, Any],
        settings: List[Setting],
        measurements: Dict[str, Dict[str, Any]],
        goal_weights: Dict[str, Union[float, Tuple[float, Dict[str, float]]]],
    ) -> str:
        """
        Add a new optimization to the machine.

        Parameters
        ----------
        name : str
            A name to quickly identify the optimization.
        description : str
            A description of the optimization. Use this description to note any details needed to
            be able to reproduce the results, other than the optimized settings.
        variables :
            The specific values for the machine variables (see Machine docstring).
        settings :
            A dictionary of settings that we want the AI to optimize, including their type and a
            relevant search range.
        measurements :
            A dictionary of values that will be provided as feedback after each experiment.
            This can be a single measurement, some subjective feedback or anything else.
            Each measurement is defined by a dict with a `values` tuple (min, max) range and
            `units` (optional).
            Notes can already be added to each experiment.
        goal_weights :
            A dictionary of goal weights. Optimyzer maximizes a weighted sum of relevant settings
            and measurements. Larger weights indicate more importance of that setting/measurement.

            Each weight can be a float (positive to maximize, negative to minimize) or a tuple
            including the weight for that setting/measurement and a second level dictionary of
            weights. Nested weights matter more as the parent setting/measurement gets closer to
            the desired direction.
        """
        if not settings:
            raise ValueError("Please provide at least one setting to optimize!")
        if not measurements:
            raise ValueError("Please provide at least one measure as feedback!")
        if not goal_weights:
            raise ValueError("Please provide at least one goal weight to optimize!")

        settings_dict = {
            setting.name: {
                "type": setting.type.value,
                "values": setting.values,
                "interval": setting.interval,
                "units": setting.units,
            }
            for setting in settings
        }
        extra_settings = {}
        for var_name, variable in self.variables.items():
            value = variables[var_name]
            var_type = "categorical"
            if variable["type"] == "num":
                # Convert to float if the variable is numerical. Leave as is for categorical
                value = float(value)
                var_type = "discrete"
            extra_settings[var_name] = {"type": var_type, "values": [value]}

        # The `knowledge` and `frozen_settings` will be computed on the API server-side
        data = {
            "optim_in": {
                "title": name,
                "description": description,
                "settings": settings_dict,
                "extra_settings_for_kt": extra_settings,
                "measurements": measurements,
                "goal_weights": goal_weights,
            },
            "machine_id": self._uid,
        }

        res = self._connection.call(CallType.POST, "machine/add_optimization", data)
        if res.status_code != 201:
            return handle_error(res)
        return res.json()

    def select_optimization(self, uid: str) -> None:
        """
        Select an optimization based on its unique identifier.
        The optimization will be loaded from the API and accessible through the `optimization`
        property of the machine instance.
        """
        self._optimization = Optimization.from_uid(uid, self._uid, self._connection)
