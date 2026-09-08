# tkinter-embed

**Install Tkinter for Embedded Python**

## Installation

### Option 1: Install with pip

1. Download [`pip.pyz`](https://bootstrap.pypa.io/pip/pip.pyz), or install pip with [`get-pip.py`](https://bootstrap.pypa.io/get-pip.py):

   ```cmd
   python.exe get-pip.py --target your_embed_folder
   ```

2. In your embedded Python folder, install Setuptools and `tkinter-embed`:

   ```cmd
   .\python.exe pip.pyz install setuptools --target .
   .\python.exe pip.pyz install tkinter-embed --target .
   ```

### Option 2: Manual installation

Download the `data.zip` file for your Python version, then copy all contents of the `cpxxx` directory into your embedded Python folder. Do not copy the `cpxxx` directory itself.

## Build Package
```cmd
python -m build --sdist
```

With uv:

```cmd
uv run --with build python -m build --sdist
```

## Test Installation
```cmd
pip install -v --target embed .\dist\tkinter_embed-1.0.0.tar.gz
```

## Publish to PyPI
```cmd
python -m twine upload dist/*
```

With uv:

```cmd
uv run --with twine python -m twine upload dist/*
```

## License

The original code in this repository is released into the public domain.
You may use, copy, modify, and distribute it for any purpose, without permission or attribution.

Tcl/Tk files included in this package are third-party components extracted from the official CPython Windows AMD64 distribution and remain subject to their original licenses. The full license text is included in the distributed package files.
