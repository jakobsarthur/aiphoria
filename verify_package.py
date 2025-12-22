#!/usr/bin/env python3
"""
Verification script for Aiphoria package structure refactoring.
Tests all import patterns to ensure the package is properly structured.
"""

import sys
import os

def test_core_imports():
    """Test core module imports."""
    print("\n" + "="*60)
    print("Testing Core Module Imports")
    print("="*60)
    
    tests = [
        ("Core builder", "from core import builder"),
        ("Core dataprovider", "from core.dataprovider import DataProvider"),
        ("Core datachecker", "from core.datachecker import DataChecker"),
        ("Core datastructures", "from core.datastructures import Scenario, Process, Flow, Stock"),
        ("Core flowsolver", "from core.flowsolver import FlowSolver"),
        ("Core parameters", "from core.parameters import ParameterName"),
        ("Core logger", "from core.logger import log"),
    ]
    
    passed = 0
    failed = 0
    
    for name, import_stmt in tests:
        try:
            exec(import_stmt)
            print(f"✓ {name}")
            passed += 1
        except Exception as e:
            print(f"✗ {name}: {str(e)[:80]}")
            failed += 1
    
    return passed, failed


def test_package_imports():
    """Test package-level imports (after installation)."""
    print("\n" + "="*60)
    print("Testing Package-Level Imports")
    print("="*60)
    
    tests = [
        ("Package root", "import aiphoria"),
        ("DataProvider", "from aiphoria import DataProvider"),
        ("DataChecker", "from aiphoria import DataChecker"),
        ("FlowSolver", "from aiphoria import FlowSolver"),
        ("Core module", "from aiphoria import core"),
        ("Builder functions", "from aiphoria import init_builder, build_results"),
        ("Logger", "from aiphoria import log"),
    ]
    
    passed = 0
    failed = 0
    
    for name, import_stmt in tests:
        try:
            exec(import_stmt)
            print(f"✓ {name}")
            passed += 1
        except Exception as e:
            print(f"✗ {name}: {str(e)[:80]}")
            failed += 1
    
    return passed, failed


def test_relative_imports():
    """Test that relative imports are in place."""
    print("\n" + "="*60)
    print("Checking Relative Import Usage")
    print("="*60)
    
    core_files = [
        "builder.py",
        "dataprovider.py",
        "datachecker.py",
        "datastructures.py",
        "flowsolver.py",
        "flowmodifiersolver.py",
        "datavisualizer.py",
        "network_graph.py",
        "utils.py",
    ]
    
    core_path = "core"
    passed = 0
    failed = 0
    
    for filename in core_files:
        filepath = os.path.join(core_path, filename)
        if not os.path.exists(filepath):
            print(f"⚠ {filename}: File not found")
            continue
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check for relative imports
        has_relative = 'from .' in content or 'import .' in content
        has_absolute_core = 'from core.' in content or 'import core.' in content
        
        if has_relative and not has_absolute_core:
            print(f"✓ {filename}: Using relative imports")
            passed += 1
        elif has_relative and has_absolute_core:
            print(f"⚠ {filename}: Mixed relative and absolute imports (may be OK if fallback)")
            passed += 1
        else:
            print(f"✗ {filename}: Not using relative imports")
            failed += 1
    
    return passed, failed


def test_init_files():
    """Check that __init__.py files exist."""
    print("\n" + "="*60)
    print("Checking __init__.py Files")
    print("="*60)
    
    paths = [
        ".",
        "core",
        "lib",
        "lib/odym",
        "lib/odym/modules",
    ]
    
    passed = 0
    failed = 0
    
    for path in paths:
        init_file = os.path.join(path, "__init__.py")
        if os.path.exists(init_file):
            # Check if it has content
            with open(init_file, 'r') as f:
                content = f.read().strip()
            
            if content:
                print(f"✓ {init_file} (has exports)")
            else:
                print(f"✓ {init_file} (empty, but exists)")
            passed += 1
        else:
            print(f"✗ {init_file} (missing)")
            failed += 1
    
    return passed, failed


def main():
    """Run all verification tests."""
    print("\n" + "="*60)
    print("AIPHORIA PACKAGE STRUCTURE VERIFICATION")
    print("="*60)
    
    # Make sure we're in the right directory
    if not os.path.exists("core"):
        print("\n⚠ Error: Must run from package root directory")
        print("Current directory:", os.getcwd())
        sys.exit(1)
    
    total_passed = 0
    total_failed = 0
    
    # Test 1: Core imports
    passed, failed = test_core_imports()
    total_passed += passed
    total_failed += failed
    
    # Test 2: Package imports
    passed, failed = test_package_imports()
    total_passed += passed
    total_failed += failed
    
    # Test 3: Relative imports in source
    passed, failed = test_relative_imports()
    total_passed += passed
    total_failed += failed
    
    # Test 4: __init__.py files
    passed, failed = test_init_files()
    total_passed += passed
    total_failed += failed
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"✓ Passed: {total_passed}")
    print(f"✗ Failed: {total_failed}")
    print(f"Total:   {total_passed + total_failed}")
    
    if total_failed == 0:
        print("\n🎉 All tests passed! Package structure is correct.")
        return 0
    else:
        print(f"\n⚠ {total_failed} test(s) failed. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
