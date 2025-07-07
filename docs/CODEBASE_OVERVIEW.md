# Codebase Overview

This project provides utilities for loading and processing point cloud data using `xarray`.

## Layout
- **xarray_lidar/** – main library containing IO helpers and spatial utilities.
- **sample_data/** – small example datasets used in tests and examples.
- **tests/** – unit tests covering IO routines.
- **scripts/** – example scripts demonstrating library usage.

## Library Highlights
- Read/write LAS/LAZ and PLY files with optional dependencies `pdal` and `plyfile`.
- Attach and transform coordinate reference systems via `pyproj`.
- Clip datasets by bounding box and convert point clouds into simple DEM rasters.

Use `read_point_cloud()` to load data and explore the additional helpers in `xarray_lidar` for processing.
