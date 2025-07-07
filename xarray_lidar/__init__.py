"""IO helpers for working with point cloud data as ``xarray`` objects."""

from pathlib import Path
import json

import numpy as np
import xarray as xr

try:
    import pdal
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    pdal = None

try:
    from plyfile import PlyData, PlyElement
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    PlyData = PlyElement = None

__package_name__ = "xarray_lidar"

SUPPORTED_FORMATS = {".las", ".laz", ".ply"}

def _load_with_pdal(file_path: str) -> xr.Dataset:
    """Internal helper to load LAS/LAZ with PDAL."""
    if pdal is None:
        raise ImportError("pdal is required to read LAS/LAZ files")

    pipeline = pdal.Pipeline(
        f"""
    {{
        "pipeline": [
            "{file_path}"
        ]
    }}
    """
    )
    pipeline.execute()
    arrays = pipeline.arrays[0]

    data_vars = {key: (["points"], np.asarray(value)) for key, value in arrays.items()}
    coords = {"points": np.arange(len(arrays["X"]))}

    return xr.Dataset(data_vars, coords)

def read_las_to_xarray(las_file_path: str) -> xr.Dataset:
    """Read a LAS/LAZ file into an ``xarray.Dataset``."""

    return _load_with_pdal(las_file_path)


def read_ply_to_xarray(ply_file_path: str) -> xr.Dataset:
    """Read a PLY point cloud file into an ``xarray.Dataset``."""

    if PlyData is None:
        raise ImportError("plyfile is required to read PLY files")

    ply = PlyData.read(ply_file_path)
    vertex = ply["vertex"]
    data_vars = {
        name: (["points"], np.asarray(vertex.data[name]))
        for name in vertex.data.dtype.names
    }
    coords = {"points": np.arange(len(vertex.data))}
    return xr.Dataset(data_vars, coords)


def read_point_cloud(file_path: str) -> xr.Dataset:
    """Load a point cloud file based on its extension."""

    ext = Path(file_path).suffix.lower()
    if ext in {".las", ".laz"}:
        return read_las_to_xarray(file_path)
    if ext == ".ply":
        return read_ply_to_xarray(file_path)
    raise ValueError(f"Unsupported file extension: {ext}")


def write_las(dataset: xr.Dataset, output_path: str) -> None:
    """Write an ``xarray.Dataset`` to a LAS/LAZ file."""

    if pdal is None:
        raise ImportError("pdal is required to write LAS/LAZ files")

    required = {"X", "Y", "Z"}
    if not required.issubset(dataset.data_vars):
        missing = ", ".join(sorted(required - set(dataset.data_vars)))
        raise ValueError(f"Dataset missing required variables: {missing}")

    arr = np.zeros(len(dataset.points), dtype=[("X", "f8"), ("Y", "f8"), ("Z", "f8")])
    for key in required:
        arr[key] = dataset[key].values

    pipeline_def = {
        "pipeline": [
            arr,
            {"type": "writers.las", "filename": output_path},
        ]
    }
    pipeline = pdal.Pipeline(json.dumps(pipeline_def))
    pipeline.execute()


def write_ply(dataset: xr.Dataset, output_path: str) -> None:
    """Write an ``xarray.Dataset`` to a PLY file."""

    if PlyElement is None:
        raise ImportError("plyfile is required to write PLY files")

    names = list(dataset.data_vars)
    dtype = [(name, "f4") for name in names]
    arr = np.zeros(len(dataset.points), dtype=dtype)
    for name in names:
        arr[name] = dataset[name].values

    element = PlyElement.describe(arr, "vertex")
    PlyData([element]).write(output_path)

