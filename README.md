<h1 align="center">xarray-lidar</h1>

<p align="center">
  <a href="https://pypi.org/project/xarray-lidar/">
    <img src="https://img.shields.io/pypi/v/xarray-lidar.svg" alt="PyPI">
  </a>
  <a href="https://github.com/yourusername/xarray-lidar/actions">
    <img src="https://github.com/yourusername/xarray-lidar/workflows/CI/badge.svg" alt="CI">
  </a>
  <a href="https://codecov.io/gh/yourusername/xarray-lidar">
    <img src="https://codecov.io/gh/yourusername/xarray-lidar/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
</p>

<p align="center">
  <strong>xarray-lidar</strong> is a Python package designed to provide functionality similar to <code>rioxarray</code> but for <strong>point cloud</strong> files. It leverages the power of <code>xarray</code> and <code>PDAL</code> to handle and process LiDAR data efficiently.
</p>

## Installation

You can install the package using pip:

```sh
pip install xarray-lidar
```

## Usage

Provide a brief example of how to use your package:

```python
import xarray-lidar

# Example usage
```

## Development

To install the package for development, clone the repository and use the following commands:

```sh
git clone https://github.com/yourusername/xarray-lidar.git
cd xarray-lidar
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

## Versioning

This project uses [Semantic Versioning](https://semver.org/). For more details, see the [CHANGELOG](./CHANGELOG.md).

## Releasing

Releases are handled automatically using [semantic-release](https://github.com/semantic-release/semantic-release). To create a new release, simply merge your changes into the `main` branch. The GitHub Action workflow will take care of the rest, including updating the version number, generating release notes, and creating a GitHub release.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
