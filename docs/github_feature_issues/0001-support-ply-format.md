# Feature: Support for PLY point cloud files

## Summary
Add read and write capabilities for the PLY file format using the `plyfile` library so that users can seamlessly open and save point cloud data in PLY.

## Motivation
Many point cloud processing tools use the PLY format. Supporting it will allow easy interoperability with 3D scanning workflows.

## Acceptance Criteria
- `read_point_cloud` detects `.ply` extension and loads data using `plyfile`.
- `write_ply` saves an `xarray.Dataset` back to a PLY file.
- Unit tests cover reading and writing a small sample PLY file.
