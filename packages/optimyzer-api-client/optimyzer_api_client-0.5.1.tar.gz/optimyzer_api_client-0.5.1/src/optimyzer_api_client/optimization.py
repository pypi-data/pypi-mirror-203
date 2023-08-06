# Copyright (c) 2020-2023, Gauss Machine Learning GmbH. All rights reserved.
# This file is part of the Optimyzer API Client, which is released under the BSD 3-Clause License.

"""
This module includes the Optimization class, which is used for running optimizations.
It also includes an auxilliary Setting class, used to define the settings that we want to optimize.
"""

from datetime import datetime as dt
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

from .api_connection import CallType, handle_error, OptimyzerConnection


class SettingType(Enum):
    """
    The available setting types: `int` (integer), `float` (floating point),
    `discrete` (a float setting which can only take specific values) and
    `categorical` (can take any value from the provided ones).
    """

    INT = "int"
    FLOAT = "float"
    DISCRETE = "discrete"
    CATEGORICAL = "categorical"


class Setting:
    """
    Settings are what define the optimization search space for Optimyzer.
    A setting can be a machine's power, feed rate or a model's dropout rate.
    Basically anything that can be tuned to achieve better results.
    """

    def __init__(
        self,
        name: str,
        set_type: SettingType,
        values: List[Any],
        interval: Optional[float] = None,
        units: str = "",
    ) -> None:
        """
        Create a Setting instance.

        Parameters
        ----------
        name : str
            A unique name for this setting.
        set_type : SettingType
            The type of setting: int, float, discrete or categorical.
        values : List[Any]
            The possible values for the setting.
            For `int` and `float` types, just the min and max values are needed.
            For `discrete` and `categorical`, the list of all possible values.
        interval : float (optional)
            The interval used for a discrete setting range.
        units : str (optional)
            The units of this setting.
        """
        self._name: str = name
        self._type: SettingType = set_type
        self._values: List[Any] = values
        if interval is None:
            self._interval = 1.0
        else:
            self._interval = interval
        self._units = units

    @property
    def name(self) -> str:
        """Return the Setting's name"""
        return self._name

    @property
    def type(self) -> SettingType:
        """Return the Setting's type"""
        return self._type

    @property
    def values(self) -> List[Any]:
        """Return the possible Setting's values"""
        return self._values

    @property
    def interval(self) -> float:
        """Return the interval used to create the possible values of a uniform discrete setting."""
        return self._interval

    @property
    def units(self) -> str:
        """Return the Setting's units"""
        return self._units


class Optimization:
    """
    Optimization class for interacting with and running optimizations.
    """

    def __init__(
        self,
        uid: str,
        name: str,
        description: str,
        variables: Dict[str, Any],
        settings: Dict[str, Setting],
        measurements: Dict[str, Dict[str, Any]],
        goal_weights: Dict[str, Union[float, Tuple[float, Dict[str, float]]]],
        connection: OptimyzerConnection,
    ) -> None:
        self._uid = uid
        self._name = name
        self._description = description
        self._variables = variables
        self._settings = settings
        self._measurements = measurements
        self._goal_weights = goal_weights
        self._connection = connection

    @property
    def name(self) -> str:
        """Return the optimization's name"""
        return self._name

    @property
    def description(self) -> str:
        """Return the optimization's description"""
        return self._description

    @property
    def variables(self) -> Dict[str, Any]:
        """Return the constant value of the machine's variables used for this optimization"""
        return self._variables

    @property
    def settings(self) -> Dict[str, Setting]:
        """Return the settings to be optimized with their possible values"""
        return self._settings

    @property
    def measurements(self) -> Dict[str, Dict[str, Any]]:
        """Return the measurements given as feedback with their expected range."""
        return self._measurements

    @property
    def goal_weights(self) -> Dict[str, Union[float, Tuple[float, Dict[str, float]]]]:
        """Return the optimization's goal weights"""
        return self._goal_weights

    @classmethod
    def from_uid(
        cls, opt_uid: str, machine_uid: str, connection: OptimyzerConnection
    ) -> "Optimization":
        """
        Get an optimization from the API using its unique identifier.
        """
        res = connection.call(
            CallType.POST,
            "machine/get_optimization_overview",
            {"opt_id": opt_uid, "machine_id": machine_uid},
        )
        if res.status_code != 200:
            handle_error(res)

        opt_dict = res.json()
        settings = {
            name: Setting(
                name,
                SettingType[setting["type"].upper()],
                setting["values"],
                setting["interval"],
                setting["units"],
            )
            for name, setting in opt_dict["settings"].items()
        }
        return cls(
            opt_uid,
            opt_dict["title"],
            opt_dict["description"],
            opt_dict["frozen_settings"],
            settings,
            opt_dict["measurements"],
            opt_dict["goal_weights"],
            connection,
        )

    def __repr__(self) -> str:
        repr_str = self.name
        repr_str += "\n" + "-" * len(repr_str)
        repr_str += "\n" + self.description
        repr_str += "\n" + ", ".join([f"{key}: {val}" for key, val in self.variables.items()])
        repr_str += "\n\nSettings:"
        for setting in self.settings.values():
            repr_str += "\n  " + f"{setting.name}: {setting.values} {setting.units}"
        repr_str += "\n\nMeasurements:"
        for name, measurement in self.measurements.items():
            repr_str += "\n  " + f"{name}: {measurement['values']} {measurement['units']}"
        repr_str += "\n\nGoal Weights:"
        for name, weight in self.goal_weights.items():
            if isinstance(weight, (int, float)):
                repr_str += "\n  " + f"{name}: {weight}"
            else:
                repr_str += "\n  " + f"{name}: {weight[0]}"
                for key, val in weight[1].items():
                    repr_str += "\n  └ " + f"{key}: {val}"

        return repr_str

    def get_suggestion(
        self, include_prediction: bool = False, include_nearest: bool = False
    ) -> Dict[str, Any]:
        """
        Get a suggestion from the AI.
        The AI will compute the next point that it would like to explore. This can be an attempt
        to explore a new area in the search space, or to exploit around previous good results.

        Parameters
        ----------
        include_prediction : bool
            Optional (default is False). If True, the API returns also the model's expectation
            and uncertainty for the suggested settings.
            This is returned under the `_prediction` key.
        include_nearest : bool
            Optional (default is False). If True, the API returns also previous settings that are
            nearest to the new suggestion.
            This is returned under the `_nearest` key.
        """
        data = {
            "num_suggestions": 1,
            "predict": include_prediction,
            "nearest": include_nearest,
            "opt_id": self._uid,
        }
        res = self._connection.call(CallType.POST, "opt/suggest_extra", data)

        if res.status_code != 200:
            handle_error(res)

        suggest_dict = res.json()[0]
        output = dict(suggest_dict["settings"])
        if include_prediction:
            output.update(_prediction=suggest_dict["prediction"])
        if include_nearest:
            output.update(_nearest=suggest_dict["nearest"])
        return output

    def report_results(
        self, settings: Dict[str, Any], results: Dict[str, Any], notes: Optional[str] = None
    ) -> None:
        """
        Report the results obtained with an experiment.
        This feedback helps the AI build a model of how the settings affect the results.

        Parameters
        ----------
        settings : Dict[str, Any]
            A dictionary of the settings used for the experiment.
            No need to pass the constant settings (frozen machine variables). They are added
            automatically here.
        results : Dict[str, Any]
            A dictionary of all the results needed to compute the optimization goal.
        notes : str
            Any relevant notes about the experiment's settings or results.
        """
        data = {
            "datapoint": {
                "settings": dict(settings, **self.variables),
                "results": results,
                "notes": notes,
                "user_email": self._connection.user_email,
                "created_on": str(dt.now()),
            },
            "opt_id": self._uid,
        }
        res = self._connection.call(CallType.PATCH, "opt/report", data)
        if res.status_code != 201:
            handle_error(res)

    def get_data(self) -> List[Dict[str, Any]]:
        """
        Return all the results obtained through the optimization.

        Each item on the returned list is a dictionary which contains the `settings` used to
        achieve the best result, any measured `results` and `notes` taken.
        """
        data = {"opt_id": self._uid}
        res = self._connection.call(CallType.POST, "opt/get_data", data)
        if res.status_code != 200:
            handle_error(res)
        return res.json()

    def get_best(self) -> Dict[str, Any]:
        """
        Return the best result obtained through the optimization.

        The returned dictionary contains the `settings` used to achieve the best result, any
        measured `results` and `notes` taken.
        """
        data = {"opt_id": self._uid}
        res = self._connection.call(CallType.POST, "opt/get_best", data)
        if res.status_code != 200:
            handle_error(res)
        return res.json()
