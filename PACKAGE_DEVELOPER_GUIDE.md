# Aiphoria Package - Developer Guide

## Quick Reference

### Installation for Development

```bash
# Clone and navigate to the project
cd /path/to/aiphoria

# Install in editable mode
pip install -e .

# Or with conda environment
conda run -n aiphoria pip install -e .
```

### Importing from the Package

#### Main exports (from root package):
```python
from aiphoria import (
    DataProvider,
    DataChecker,
    FlowSolver,
    Scenario,
    Process,
    Flow,
    Stock,
    Indicator,
    ParameterName,
    ParameterFillMethod,
    init_builder,
    build_results,
    log,
)
```

#### Core module imports:
```python
from aiphoria.core import builder
from aiphoria.core.dataprovider import DataProvider
from aiphoria.core.logger import log
```

#### Working with the builder:
```python
from aiphoria import init_builder, build_results
from aiphoria.parameters import ParameterName

# Initialize builder
init_builder(path_to_cache="./cache", use_cache=False)

# Build and solve scenarios
model_params, scenarios, colors = build_results("data/example_data.xlsx")
```

### Package Structure

```
aiphoria/
├── __init__.py                 # Package root - exports main API
├── core/
│   ├── __init__.py            # Core module exports
│   ├── builder.py             # Main orchestrator
│   ├── dataprovider.py        # Data loading from Excel
│   ├── datachecker.py         # Data validation
│   ├── datastructures.py      # Core data classes
│   ├── datavisualizer.py      # Visualization
│   ├── flowsolver.py          # Flow solving logic
│   ├── flowmodifiersolver.py  # Flow modifications
│   ├── logger.py              # Logging utilities
│   ├── network_graph.py       # Network visualization
│   ├── parameters.py          # Parameter definitions
│   ├── types.py               # Type definitions
│   ├── utils.py               # Utility functions
│   └── visualizer_parameters.py
├── lib/
│   ├── __init__.py
│   └── odym/                  # ODYM library (external)
│       ├── __init__.py
│       └── modules/
│           ├── __init__.py
│           ├── ODYM_Classes.py
│           ├── ODYM_Functions.py
│           └── dynamic_stock_model.py
└── data/
    └── example_data.xlsx      # Example input file
```

### Working with Core Modules

Each core module has a specific responsibility:

**builder.py** - Orchestrates the workflow:
```python
from aiphoria.core import builder

builder.init_builder(path_to_cache="./cache")
model_params, scenarios, colors = builder.build_results("data/input.xlsx")
```

**dataprovider.py** - Loads data from Excel:
```python
from aiphoria.core.dataprovider import DataProvider

dp = DataProvider("data/input.xlsx")
processes = dp.get_processes()
flows = dp.get_flows()
```

**datachecker.py** - Validates data:
```python
from aiphoria.core.datachecker import DataChecker

dc = DataChecker(dataprovider)
dc.check_model_data(model_params)
```

**flowsolver.py** - Solves material flows:
```python
from aiphoria.core.flowsolver import FlowSolver

fs = FlowSolver()
fs.solve(scenario)
```

**logger.py** - Centralized logging:
```python
from aiphoria.core.logger import log

log.info("Starting analysis")
log.warning("Check this data")
```

### Import Patterns Used

All core modules use relative imports for intra-module imports:

```python
# In core/builder.py
from .datachecker import DataChecker      # Relative import
from .logger import log                    # Relative import
from .parameters import ParameterName      # Relative import

# For external lib imports with fallback
try:
    from ..lib.odym.modules import DynamicStockModel
except ImportError:
    from lib.odym.modules import DynamicStockModel
```

This pattern provides maximum flexibility:
- Works when package is installed (`pip install -e .`)
- Works when running from package directory
- Works in Jupyter notebooks and scripts

### Common Tasks

#### Run the example notebook:
```bash
cd /path/to/aiphoria
conda run -n aiphoria jupyter notebook example.ipynb
```

#### Create a new scenario:
```python
from aiphoria import DataProvider, FlowSolver

# Load data
dp = DataProvider("data/input.xlsx")

# Get processes and flows
processes = dp.get_processes()
flows = dp.get_flows()

# Create and solve scenario
fs = FlowSolver()
# ... configure and solve
```

#### Add logging to your code:
```python
from aiphoria.core.logger import log

log.debug("Detailed information")
log.info("General information")
log.warning("Warning message")
log.error("Error occurred")
```

#### Configure parameters:
```python
from aiphoria import ParameterName

# Access parameter names
start_year = ParameterName.StartYear
end_year = ParameterName.EndYear
output_path = ParameterName.OutputPath
```

#### Manage output directory:
```python
from aiphoria.core.utils import (
    create_output_directory,
    get_output_directory,
    get_output_file_path
)

# Set output directory (deletes existing, creates new)
output_dir = create_output_directory("./output")
print(f"Output will be saved to: {output_dir}")

# All subsequent output operations use this directory
visualizer.visualize_sankey_diagrams()  # ✓ Saves to output_dir

# Get path for custom output files
results_file = get_output_file_path("results.csv")
scenario_file = get_output_file_path("report.html", scenario_name="Scenario_A")

# Save your files
with open(results_file, 'w') as f:
    f.write("my data")
```

See [OUTPUT_DIRECTORY_MANAGEMENT.md](./OUTPUT_DIRECTORY_MANAGEMENT.md) for detailed guide.

### Testing Imports

Verify the package structure is working:

```bash
# Test core imports
python -c "from aiphoria.core import builder; print('✓ Core imports OK')"

# Test package-level imports (requires pip install -e .)
python -c "from aiphoria import DataProvider; print('✓ Package imports OK')"

# Run full verification
python verify_package.py
```

### Dependencies

**Required:**
- numpy
- pandas
- openpyxl
- scipy

**Optional:**
- matplotlib (for visualization)
- plotly (for interactive plots)
- IPython (for Jupyter support)

Install all dependencies:
```bash
pip install -e ".[dev]"
```

### Troubleshooting

**Import Error: "No module named 'aiphoria'"**
- Solution: Run `pip install -e .` from the package root

**Import Error: "attempted relative import beyond top-level package"**
- Solution: Ensure you're importing as `from aiphoria.core import X` not `from core import X`

**Module not found errors in IDE**
- Solution: Make sure your IDE's Python interpreter is set to the conda environment

### Contributing

When adding new modules to core:

1. Create the module file in `core/`
2. Add relative imports for other core modules
3. Update `core/__init__.py` to export new classes/functions
4. Update root `__init__.py` if it's a commonly-used API

Example new module:

```python
# core/my_new_module.py
from .logger import log
from .datastructures import Scenario

class MyNewClass:
    def __init__(self):
        log.info("Initializing MyNewClass")
```

Then add to `core/__init__.py`:
```python
from .my_new_module import MyNewClass

__all__ = [
    # ... existing exports ...
    "MyNewClass",
]
```

---

**Last Updated**: December 22, 2025
**Package Version**: 0.1.0
