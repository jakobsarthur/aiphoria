# Package Structure Migration Guide

This document describes the changes made to convert Aiphoria into a proper Python package with modern import structure.

## What Changed

### Before (Local Imports)
Previously, imports used absolute paths that relied on the current working directory or system path manipulation:

```python
# Old way
from core.datastructures import Scenario
from core.parameters import ParameterName
from lib.odym.modules.ODYM_Classes import MFAsystem
```

### After (Package Imports)
Now, with the proper package structure, you can use:

```python
# New way - Using package imports
from aiphoria.core import Scenario, ParameterName
from aiphoria.core.builder import build_results
from aiphoria.lib.odym.modules import ODYM_Classes

# Or in notebooks where you're in the workspace root:
from core.datastructures import Scenario  # Still works if workspace is in PYTHONPATH
```

## File Structure

The new package structure is:

```
aiphoria/
├── __init__.py                 # Package initialization with main exports
├── pyproject.toml             # Modern Python package configuration
├── setup.py                   # Setuptools configuration (fallback)
├── MANIFEST.in                # Package data includes
├── core/
│   ├── __init__.py           # Core module exports
│   ├── builder.py
│   ├── dataprovider.py
│   ├── datachecker.py
│   ├── datastructures.py
│   ├── flowsolver.py
│   ├── flowmodifiersolver.py
│   ├── datavisualizer.py
│   ├── network_graph.py
│   ├── parameters.py
│   ├── types.py
│   ├── utils.py
│   ├── logger.py
│   ├── visualizer_parameters.py
│   └── [data folders]
├── lib/
│   ├── __init__.py
│   └── odym/
│       ├── __init__.py
│       └── modules/
│           ├── __init__.py
│           ├── ODYM_Classes.py
│           ├── ODYM_Functions.py
│           ├── dynamic_stock_model.py
│           └── test/
└── docs/
    └── [documentation files]
```

## Installation

### Development Installation
To install the package in development mode (for local development):

```bash
pip install -e .
```

### Regular Installation
To install the package normally:

```bash
pip install .
```

### From Repository
To install directly from the GitHub repository:

```bash
pip install git+https://github.com/jakobsarthur/aiphoria.git
```

## Using the Package

### In Python Scripts
After installation:

```python
from aiphoria import DataProvider, DataChecker, build_results
from aiphoria.core import Scenario, ParameterName
from aiphoria.lib.odym.modules import ODYM_Classes as msc

# Use the package
model_params, scenarios, colors = build_results("data/example_data.xlsx")
```

### In Jupyter Notebooks
When running from the workspace root:

```python
# If workspace is in PYTHONPATH
from core import builder
from core.datastructures import Scenario

# Or use full package import
from aiphoria.core import builder
from aiphoria.core.datastructures import Scenario
```

### In Example Notebook
The `example.ipynb` notebook uses relative imports which work because it's in the workspace root:

```python
from core import builder
from core.logger import log
from core.datavisualizer import DataVisualizer
```

This works because the workspace root is treated as the package root when running from within the notebook.

## Relative Imports Within the Package

All internal imports within the package (between core modules) now use relative imports:

```python
# In aiphoria/core/builder.py
from .dataprovider import DataProvider      # Relative import
from .logger import log                     # Relative import
from ..lib.odym.modules import ODYM_Classes # Relative import to parent package
```

## Benefits of the New Structure

1. **Standard Python Packaging**: Follows PEP 420/420 for namespace packages
2. **Better IDE Support**: IDEs can better understand the structure and provide better autocomplete
3. **Easier Distribution**: Can be distributed via PyPI
4. **Clear Dependencies**: Dependencies are properly declared in `pyproject.toml`
5. **Installable**: Can be installed as a proper package with `pip install`
6. **Import Flexibility**: Works with both absolute and relative imports

## Migration Checklist

If you're updating existing code:

- [ ] Update absolute imports to use the `aiphoria.core` package prefix
- [ ] Or ensure workspace root is in `PYTHONPATH` for backward compatibility
- [ ] Install the package with `pip install -e .` for development
- [ ] Update any documentation with new import examples
- [ ] Test imports both ways to ensure compatibility

## Backward Compatibility

The old import style will still work if you:
1. Add the workspace root to `PYTHONPATH`
2. Run from the workspace root directory
3. Have the package installed with `pip install -e .`

For new code, please use the proper package imports shown above.
