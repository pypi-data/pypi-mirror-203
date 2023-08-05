# Copyright (c) 2020-2023, Gauss Machine Learning GmbH. All rights reserved.
# This file is part of the Optimyzer API Client, which is released under the BSD 3-Clause License.

"""
This module includes the Optimyzer API Client class for interacting with the Optimyzer API
and a few auxilliary functions.
"""
from typing import Dict, List, Optional

from .api_connection import CallType, handle_error, OptimyzerConnection
from .machine import Machine

SERVER_URL = "https://api.optimyzer.ai/"


class OptimyzerClient:
    """
    The Optimyzer API Client class.
    It is used to interact with Optimyzer's API to create and run optimizations.
    """

    def __init__(self, connection: OptimyzerConnection) -> None:
        self._connection = connection
        self._machine: Optional[Machine] = None

    @classmethod
    def from_login(
        cls, username: str, password: str, server_url: str = SERVER_URL
    ) -> "OptimyzerClient":
        """
        Create an instance with the login info.

        Parameters
        ----------
        username : str
            The user's email address.
        password : str
            The user's password.
        """
        connection = OptimyzerConnection.from_login(username, password, server_url)
        return cls(connection)

    @classmethod
    def from_credentials(cls, filepath: str, server_url: str = SERVER_URL) -> "OptimyzerClient":
        """
        Create an instance with the login info stored in the filepath.

        Parameters
        ----------
        filepath : str
            The path to the JSON file containing the login information.
            The file should have key-value pairs for `username` and `password`.
        """
        connection = OptimyzerConnection.from_credentials(filepath, server_url)
        return cls(connection)

    @property
    def machine(self) -> Machine:
        """
        Return the active machine.
        Raises a RuntimeError is no machine has been selected.
        """
        if self._machine is None:
            raise RuntimeError(
                "No machine selected! Please select a machine using its uniqe identifier first."
            )
        return self._machine

    def add_machine(self, name: str, description: str, variables: Dict[str, Dict[str, str]]) -> str:
        """
        Create a new machine within the user's group.

        Machines provide a useful way of clustering optimizations for knowledge transfer.
        For example, many optimizations are run on a laser cutting machine for different materials.
        Optimyzer transfers the experience from previous optimizations in a machine to each new
        optimization created.

        The variables indicate what changes between optimizations. For example, that can be the
        material type and material thickness.

        Parameters
        ----------
        name : str
            A unique name to identify the machine.
        description : str
            A description of the machine (group of optimizations).
        variables : Dict[str, Dict[str, str]]
            A dictionary of variables for the machine.
            Each variable is a <key, value> pair, where the value is a dictionary containing:
            - The variable's type: "cat" for categorical or "num" for numerical
            - The variable's units (optional): a string

        Returns
        -------
        str
            The ID of the newly created machine.
        """
        machine = {
            "name": name,
            "description": description,
            "variables": variables,
            "optimizations": [],
        }

        # Submit the new machine through the API
        res = self._connection.call(CallType.POST, "group/add_machine", machine)
        if res.status_code != 201:
            handle_error(res)
        return str(res.json())

    def get_all_machines(self) -> List[Dict[str, str]]:
        """
        Get a list of all the machines in the group.

        Returns
        -------
        List[Dict[str, str]]
            A list of dictionaries containing the unique ID and name of each machine.
        """
        res = self._connection.call(CallType.POST, "group/get_all_machines")
        if res.status_code != 200:
            handle_error(res)
        return res.json()

    def select_machine(self, uid: str) -> None:
        """
        Select a machine based on its unique identifier.
        The machine will be loaded from the API and accessible through the `machine` property of
        the client instance.
        """
        self._machine = Machine.from_uid(uid, self._connection)
