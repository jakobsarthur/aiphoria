#!/usr/bin/env python
"""Setup script for Aiphoria package."""

from setuptools import setup, find_packages

setup(
    name="aiphoria",
    version="0.1.0",
    packages=find_packages(include=["aiphoria", "aiphoria.*", "lib", "lib.*"]),
    python_requires=">=3.9",
    install_requires=[
        "numpy==1.26.4",
        "openpyxl==3.1.3",
        "pandas==2.2.2",
        "Pillow==10.3.0",
        "plotly==5.24.1",
        "scipy",
        "matplotlib",
        "xlrd",
        "xlwt",
        "tqdm",
        "myst-parser",
        "sphinx-rtd-theme",
        "IPython",
        "xlsxwriter==3.2.5"
    ],
    author="Arthur Jakobs",
    author_email="artos.jakobs@psi.ch",
    maintainer="Arthur Jakobs",
    maintainer_email="artos.jakobs@psi.ch",
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
        classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="material flow analysis ODYM dynamic stock modeling industrial ecology",
)
