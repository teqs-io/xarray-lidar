<h1 align="center">xarray-pdal</h1>

<p align="center">
  <a href="https://pypi.org/project/xarray-pdal/">
    <img src="https://img.shields.io/pypi/v/xarray-pdal.svg" alt="PyPI">
  </a>
  <a href="https://github.com/yourusername/xarray-pdal/actions">
    <img src="https://github.com/yourusername/xarray-pdal/workflows/CI/badge.svg" alt="CI">
  </a>
  <a href="https://codecov.io/gh/yourusername/xarray-pdal">
    <img src="https://codecov.io/gh/yourusername/xarray-pdal/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
</p>

<p align="center">A brief description of your package.</p>

<p align="center">
  <strong>xarray-pdal</strong> is a Python package designed to provide functionality similar to <code>rioxarray</code> but for <strong>point cloud</strong> files. It leverages the power of <code>xarray</code> and <code>PDAL</code> to handle and process LiDAR data efficiently.
</p>

## Installation

You can install the package using pip:

```sh
pip install xarray-pdal
```

## Usage

Provide a brief example of how to use your package:

```python
import xarray_pdal

# Example usage
```

## Development

To install the package for development, clone the repository and use the following commands:

```sh
git clone https://github.com/yourusername/xarray-pdal.git
cd xarray-pdal
pip install -e .
```

## Building and Publishing

To build the package, use the following command:

```sh
python setup.py sdist bdist_wheel
```

To upload the package to PyPI, use the following command:

```sh
twine upload dist/*
```

Make sure you have `twine` installed (`pip install twine`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
