# Copyright (c) 2020-2023, Gauss Machine Learning GmbH. All rights reserved.
# This file is part of the Optimyzer API Client, which is released under the BSD 3-Clause License.

"""
This module includes the OptimyzerConnection class, used to interact with the API.
"""
from enum import Enum
from typing import Any, Optional
import json
import requests  # type: ignore

from .secret_loader import get_secrets


class CallType(Enum):
    """
    A handy class to indicate which type of API calls are available.
    Shorter version than typing `requests.post`.
    """

    DELETE = requests.delete
    PATCH = requests.patch
    POST = requests.post


class OptimyzerConnection:
    """
    The OptimyzerConnection class, used to interact with the API.
    """

    def __init__(self, server_url: str, api_token: str, user_email: str) -> None:
        self._api_url = server_url
        self._api_token = api_token
        self._user_email = user_email

    @classmethod
    def from_login(cls, username: str, password: str, server_url: str) -> "OptimyzerConnection":
        """
        Create an instance with the login info.

        Parameters
        ----------
        username : str
            The user's email address.
        password : str
            The user's password.
        """
        api_token = login(username, password, server_url)
        return cls(server_url, api_token, username)

    @classmethod
    def from_credentials(cls, filepath: str, server_url: str) -> "OptimyzerConnection":
        """
        Create an instance with the login info stored in the filepath.

        Parameters
        ----------
        filepath : str
            The path to the JSON file containing the login information.
            The file should have key-value pairs for `OPTIMYZER_USERNAME` and `OPTIMYZER_PASSWORD`.
        """
        cred = get_secrets(
            filepath, {"OPTIMYZER_USERNAME": (str, None), "OPTIMYZER_PASSWORD": (str, None)}
        )

        return OptimyzerConnection.from_login(
            cred["OPTIMYZER_USERNAME"], cred["OPTIMYZER_PASSWORD"], server_url
        )

    @property
    def user_email(self) -> str:
        """Return the user's email for the active connection."""
        return self._user_email

    def call(
        self, method: CallType, endpoint: str, data: Optional[Any] = None, timeout: float = 5.0
    ) -> requests.Response:
        """
        Call an API endpoint using the selected method and pass the data
        """
        if data is None:
            res = method(  # type: ignore
                self._api_url + endpoint,
                headers={"Authorization": f"Bearer {self._api_token}"},
                timeout=timeout,
            )
        else:
            res = method(  # type: ignore
                self._api_url + endpoint,
                data=json.dumps(data),
                headers={"Authorization": f"Bearer {self._api_token}"},
                timeout=timeout,
            )
        return res


def check_response(res: requests.Response, expected_code: int = 200) -> None:
    """
    Check the response from the API. The default expected code is 200.
    Raises a PermissionError for a 401 response and a RuntimeError for any code
    other than the expected.

    Parameters
    ----------
    res : requests.Response
        The response received from the `requests` call.
    expected_code : int
        The expected response code. By default: 200.
    """
    if res.status_code == 401:
        raise PermissionError(str(res.json()))
    if res.status_code == 500:
        raise RuntimeError("500: Server error")
    if res.status_code != expected_code:
        raise RuntimeError(str(res.json()))


def login(username: str, password: str, server_url: str) -> Any:
    """
    Logins to the Optimyzer API and returns the access token, if successful.
    """
    auth = requests.post(
        server_url + "auth/login", data={"username": username, "password": password}, timeout=5
    )
    check_response(auth)
    return auth.json()["access_token"]


def handle_error(res: requests.Response):
    """
    Handle various error messages from the API.
    """
    if res.status_code == 401:
        raise RuntimeError("The API token timed out!")

    if res.status_code == 500:
        raise RuntimeError(f"Something went wrong! {res.text}")

    detail = res.json().get("detail", None)
    if detail:
        if isinstance(detail, str):
            error_msg = detail
        elif isinstance(detail, list):
            error_msgs = []
            for sub_detail in detail:
                error_msgs.append(f"{sub_detail['type']}: {sub_detail['msg']}")
            error_msg = ", ".join(error_msgs)
        else:
            error_msg = f"{detail['type']}: {detail['msg']}"
    else:
        error_msg = ""

    raise RuntimeError(f"Something went wrong! {error_msg}")
