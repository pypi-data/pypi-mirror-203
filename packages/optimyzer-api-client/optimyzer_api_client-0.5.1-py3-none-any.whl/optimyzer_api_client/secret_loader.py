# Copyright (c) 2020-2023, Gauss Machine Learning GmbH. All rights reserved.
# This file is part of the Optimyzer API Client, which is released under the BSD 3-Clause License.

"""
This utilities can be used to load secrets both locally and after deploying to the cloud.
"""
import json
import os
from typing import Any, Dict, Tuple, Union


class JSONType(dict):
    """A simple wrapper that can load dictionaries both as `dict` and as a json string"""

    def __init__(self, secret_json: Union[dict, str]):
        if isinstance(secret_json, dict):
            super().__init__(**secret_json)
        else:
            super().__init__(**json.loads(secret_json))


def get_secrets(filepath: str, secrets: Dict[str, Tuple[type, Any]]) -> Dict[str, Any]:
    """
    This function tries to load the required settings from a given `filepath`.
    If the file is not found, the function will look for the secrets in the environment variables.

    Parameters
    ----------
    filepath : str
        The path to the file containing the secrets. Use this for local development.
        When deploying, the secrets should be stored as environment variables.
    secrets : Dict[str, Tuple[Type, Any]]
        A dictionary with the `key` is the secret's name and the `value` is a Tuple defining
        the type expected and a possible default value (or None)
    """
    if os.path.exists(filepath):
        # Load the secret from the config file
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            read_secrets = {}
            for secret, (secret_type, secret_default) in secrets.items():
                value = data.get(secret, None)
                if value is None:
                    # This secret isn't in the file. Is there a default provided?
                    if secret_default is not None:
                        value = secret_default
                    else:
                        raise RuntimeError(
                            f"Expected to get a {secret} secret, but none was found."
                        )
                read_secrets[secret] = secret_type(value)
    else:
        # Load the secrets from the environment
        read_secrets = {}
        for secret, (secret_type, secret_default) in secrets.items():
            value = os.environ.get(secret, None)
            if value is None:
                # This secret isn't in the environment variables. Is there a default provided?
                if secret_default is not None:
                    value = secret_default
                else:
                    raise RuntimeError(
                        f"Expected to get a {secret} environmental variable, but none was found."
                    )
            read_secrets[secret] = secret_type(value)
    return read_secrets
