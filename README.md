# tkinter-embed

**Install Tkinter for Embedded Python**

## Prerequisites

1. Download `pip.pyz` or install pip:
   - Option 1: Download `pip.pyz` from https://bootstrap.pypa.io/pip/pip.pyz
   - Option 2: Install pip using get-pip.py
     - Download from: https://bootstrap.pypa.io/get-pip.py
     - Run with your embedded Python: `python.exe get-pip.py --target your_embed_folder`

2. Install Setuptools first.

The following examples use the pip.pyz method for installation.

## Installation Steps

Navigate to your embedded Python folder and run:
```cmd
.\python pip.pyz install setuptools --target .
.\python pip.pyz install tkinter-embed --target .
```

## Build Package
```cmd
python -m build --sdist
```

## Test Installation
```cmd
pip install -v --target embed .\dist\tkinter_embed-1.0.0.tar.gz
```

## Publish to PyPI
```cmd
python -m twine upload dist/*
```
