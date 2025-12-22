t# Quick Reference: Aiphoria Package Structure

## Package Import Patterns

### Main Entry Points

```python
# Import the entire package
import aiphoria

# Import main classes
from aiphoria import (
    DataProvider,
    DataChecker,
    FlowSolver,
    Scenario,
    Process,
    Flow,
    Stock,
    Indicator,
)

# Import builder functions
from aiphoria import init_builder, build_results

# Import utilities
from aiphoria import log, ParameterName, ParameterFillMethod
```

### Core Module Direct Imports

```python
# Import from core submodule
from aiphoria.core import builder
from aiphoria.core import parameters
from aiphoria.core import datastructures
from aiphoria.core import logger

# Import specific classes
from aiphoria.core.dataprovider import DataProvider
from aiphoria.core.datachecker import DataChecker
from aiphoria.core.flowsolver import FlowSolver
```

### Legacy/Development Imports (still working)

When running from the package root directory:

```python
# These still work for backward compatibility
from core import builder
from core.dataprovider import DataProvider
from core.parameters import ParameterName
```

## Module Organization

### Core Modules (`aiphoria.core`)

| Module | Purpose | Key Classes |
|--------|---------|------------|
| `builder.py` | Orchestrates data loading and solving | `init_builder()`, `build_results()` |
| `dataprovider.py` | Reads data from Excel files | `DataProvider` |
| `datachecker.py` | Validates and checks data | `DataChecker` |
| `datastructures.py` | Core data structures | `Scenario`, `Process`, `Flow`, `Stock` |
| `flowsolver.py` | Solves flow equations | `FlowSolver` |
| `flowmodifiersolver.py` | Handles flow modifiers | `FlowModifierSolver` |
| `datavisualizer.py` | Creates visualizations | `DataVisualizer` |
| `network_graph.py` | Generates network graphs | `NetworkGraph` |
| `parameters.py` | Parameter definitions | `ParameterName`, `ParameterFillMethod` |
| `types.py` | Type definitions | `FunctionType`, `ChangeType` |
| `logger.py` | Logging utilities | `log` |
| `utils.py` | Utility functions | `setup_*` functions |

### Library Modules (`aiphoria.lib`)

```
lib/
├── odym/
│   └── modules/
│       ├── ODYM_Classes.py      # Material Flow Analysis classes
│       ├── ODYM_Functions.py    # Utility functions
│       └── dynamic_stock_model.py # Stock modeling
```

## Installation & Setup

### Development Installation (Recommended)

```bash
cd /path/to/aiphoria
pip install -e .
```

This installs the package in editable mode, allowing imports from anywhere.

### Regular Installation

```bash
pip install /path/to/aiphoria
```

### Dependencies

```bash
# Core dependencies
pip install numpy pandas matplotlib scipy

# ODYM dependencies
pip install openpyxl xlrd

# Optional: For advanced features
pip install pypandoc
```

## Common Usage Examples

### Loading Data

```python
from aiphoria import DataProvider

provider = DataProvider("data/example_data.xlsx")
model_params = provider.get_model_params()
processes = provider.get_processes()
flows = provider.get_flows()
stocks = provider.get_stocks()
```

### Checking Data

```python
from aiphoria import DataChecker

checker = DataChecker(provider)
scenario = checker.build_scenario(model_params)
```

### Solving Flows

```python
from aiphoria import FlowSolver

solver = FlowSolver(scenario)
solver.solve()
```

### Building Complete Results

```python
from aiphoria import init_builder, build_results

init_builder(path_to_cache="./cache", use_cache=False)
model_params, scenarios, colors = build_results("data/example_data.xlsx")
```

### Visualization

```python
from aiphoria.core import DataVisualizer, NetworkGraph

visualizer = DataVisualizer()
visualizer.visualize(scenario)

graph = NetworkGraph()
graph.create_network_graph(scenario_data)
```

## Module Relationships

```
dataprovider → datastructures
     ↓
datachecker → types, parameters
     ↓
flowsolver → flowmodifiersolver
     ↓
datavisualizer
     ↓
network_graph
     ↓
builder (orchestrates all)
```

## Relative Imports in Code

All internal code uses relative imports:

```python
# In aiphoria/core/builder.py
from .dataprovider import DataProvider
from .datachecker import DataChecker
from .flowsolver import FlowSolver

# In aiphoria/core/datastructures.py
from .parameters import ParameterName
from .types import FunctionType

# Accessing lib from core
from ..lib.odym.modules import ODYM_Classes
```

## Testing Imports

Verify the package structure with:

```bash
python -c "from aiphoria import DataProvider; print('✓ Package structure working')"
python -c "from aiphoria.core import builder; print('✓ Core module working')"
python -c "from aiphoria import init_builder, build_results; print('✓ Main functions working')"
```

---

For more details, see `REFACTORING_SUMMARY.md`
