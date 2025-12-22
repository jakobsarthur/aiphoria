"""
Core module containing main classes and utilities for Aiphoria.

This module provides:
- Data handling: DataProvider, DataChecker
- Data structures: Scenario, Process, Flow, Stock
- Model solving: FlowSolver, Builder
- Visualization: DataVisualizer, NetworkGraph
- Logging and utilities
"""

from .builder import (
    init_builder,
    build_results,
    build_dataprovider,
    build_datachecker,
    build_and_solve_scenarios,
)
from .dataprovider import DataProvider
from .datachecker import DataChecker
from .datastructures import (
    Scenario,
    ScenarioData,
    Process,
    Flow,
    Stock,
    Indicator,
)
from .flowsolver import FlowSolver
from .parameters import ParameterName, ParameterFillMethod, StockDistributionType
from .datavisualizer import DataVisualizer
from .network_graph import NetworkGraph
from .logger import log
from .utils import (
    setup_current_working_directory,
    setup_odym_directories,
    create_output_directory,
)

__all__ = [
    "init_builder",
    "build_results",
    "build_dataprovider",
    "build_datachecker",
    "build_and_solve_scenarios",
    "DataProvider",
    "DataChecker",
    "Scenario",
    "ScenarioData",
    "Process",
    "Flow",
    "Stock",
    "Indicator",
    "FlowSolver",
    "DataVisualizer",
    "NetworkGraph",
    "ParameterName",
    "ParameterFillMethod",
    "StockDistributionType",
    "log",
    "setup_current_working_directory",
    "setup_odym_directories",
    "create_output_directory",
]
