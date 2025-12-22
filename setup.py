#!/usr/bin/env python
"""Setup script for Aiphoria package."""

from setuptools import setup, find_packages

setup(
    name="aiphoria",
    version="0.1.0",
    packages=find_packages(include=["aiphoria", "aiphoria.*", "lib", "lib.*"]),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.9",
        "pandas>=1.0",
        "matplotlib>=3.0",
        "scipy>=0.14",
        "openpyxl>=2.6",
        "xlrd>=1.0",
        "plotly>=4.0",
        "Pillow>=8.0",
        "tqdm>=4.0",
        "IPython>=7.0",
    ],
    author="Arthur Jakobs",
    author_email="arthur.jakobs@example.com",
    maintainer="Arthur Jakobs",
    maintainer_email="arthur.jakobs@example.com",
    description="Advanced Industrial Process Flow Handling and ODYM-based Resource Information Assistant",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jakobsarthur/aiphoria",
    project_urls={
        "Documentation": "https://aiphoria.readthedocs.io",
        "Repository": "https://github.com/jakobsarthur/aiphoria.git",
        "Bug Tracker": "https://github.com/jakobsarthur/aiphoria/issues",
    },
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    keywords="material flow analysis ODYM dynamic stock modeling industrial ecology",
)
