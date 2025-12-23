"""
Aiphoria - Advanced Industrial Process Flow Handling and ODYM-based Resource Information Assistant

A Python package for material flow analysis and dynamic stock modeling using ODYM.

Attribution
-----------
This project is a fork of the original aiphoria project created by the European Forest Institute.

Original Project:
    - Authors: Cleo Orfanidou, Janne Järvikylä
    - Organization: European Forest Institute (EFI)
    - License: MIT
    - Repository: https://github.com/EuropeanForestInstitute/aiphoria

Current Fork (2025):
    - Maintained by: Arthur Jakobs
    - License: MIT (same as original)
    - Repository: https://github.com/jakobsarthur/aiphoria

For more information on attribution and contributors, see:
    - LICENSE file: Copyright and license terms
    - CONTRIBUTORS.md: Detailed list of contributors
    - FORK_ATTRIBUTION_GUIDE.md: Attribution guidelines

Licensed under the MIT License.
"""

__version__ = "0.1.0"
__author__ = "Arthur Jakobs"

# Import main modules
from . import core

# Import commonly used classes and functions
from .core.builder import (
    init_builder,
    build_results,
    build_dataprovider,
    build_datachecker,
)
from .core.dataprovider import DataProvider
from .core.datachecker import DataChecker
from .core.datastructures import (
    Scenario,
    ScenarioData,
    Process,
    Flow,
    Stock,
    Indicator,
)
from .core.parameters import ParameterName, ParameterFillMethod
from .core.utils import (
    create_output_directory,
    get_output_directory,
    set_output_directory,
    get_output_file_path,
)
from .core.logger import log

__all__ = [
    "core",
    "init_builder",
    "build_results",
    "build_dataprovider",
    "build_datachecker",
    "DataProvider",
    "DataChecker",
    "Scenario",
    "ScenarioData",
    "Process",
    "Flow",
    "Stock",
    "Indicator",
    "ParameterName",
    "ParameterFillMethod",
    "create_output_directory",
    "get_output_directory",
    "set_output_directory",
    "get_output_file_path",
    "log",
]
