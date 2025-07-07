# Feature: Coordinate Reprojection

## Summary
Expose helper methods for reprojecting point cloud coordinates between different CRS using `pyproj`.

## Motivation
Point clouds often come in different coordinate reference systems. Built-in reprojection would simplify data preparation workflows.

## Acceptance Criteria
- New `reproject(dataset, dst_crs)` function that returns a dataset in the requested CRS.
- Support specifying CRS strings and EPSG codes.
- Unit tests with sample data verifying coordinate transformation.
