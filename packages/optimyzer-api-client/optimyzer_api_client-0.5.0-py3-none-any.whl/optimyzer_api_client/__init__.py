# Copyright (c) 2020-2023, Gauss Machine Learning GmbH. All rights reserved.
# This file is part of the Optimyzer API Client, which is released under the BSD 3-Clause License.

"""
Optimyzer API Client -- This is the Python API Client for Optimyzer
"""
# Optimyzer uses semantic versioning according to PEP-0440:
# https://www.python.org/dev/peps/pep-0440/
__version__ = "0.5.0"

from .client import OptimyzerClient
from .optimization import Setting, SettingType
