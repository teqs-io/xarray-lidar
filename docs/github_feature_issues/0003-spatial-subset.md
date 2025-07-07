# Feature: Spatial Subset Operations

## Summary
Provide clipping and cropping utilities for point cloud datasets based on bounding boxes or polygon geometries.

## Motivation
Users often need to extract a subset of points for analysis or visualization. Having helper functions avoids manual filtering of the dataset.

## Acceptance Criteria
- `clip(dataset, bounds)` where bounds can be a bounding box or shapely geometry.
- `crop(dataset, bounds)` that returns a new dataset containing only points within the region.
- Tests verifying correct behaviour for 2D bounding boxes.
