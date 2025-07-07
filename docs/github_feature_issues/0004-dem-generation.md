# Feature: Digital Elevation Model Generation

## Summary
Create utilities that transform a point cloud into a raster Digital Elevation Model (DEM) using interpolation or gridding methods.

## Motivation
Generating DEMs from point clouds is a common step for further geospatial analysis. Built-in helpers streamline this workflow without relying on external tools.

## Acceptance Criteria
- `to_dem(dataset, resolution)` returns an xarray `DataArray` representing the DEM.
- Support simple interpolation (nearest neighbour) as an initial implementation.
- Include documentation and a usage example in the README.
