import numpy as np
import xarray as xr
import pytest
Polygon = pytest.importorskip("shapely.geometry").Polygon

import xarray_lidar as xl


def test_set_and_get_crs():
    ds = xr.Dataset({"X": ("points", [0, 1]), "Y": ("points", [0, 1])})
    ds = xl.set_crs(ds, "EPSG:4326")
    assert xl.get_crs(ds) == "EPSG:4326"


def test_to_crs_identity():
    ds = xr.Dataset({"X": ("points", [0]), "Y": ("points", [0])})
    ds = xl.set_crs(ds, "EPSG:4326")
    out = xl.to_crs(ds, "EPSG:4326")
    assert np.allclose(out["X"], ds["X"]) and np.allclose(out["Y"], ds["Y"])


def test_clip_bbox():
    ds = xr.Dataset({
        "X": ("points", [0, 5, 10]),
        "Y": ("points", [0, 5, 10]),
        "Z": ("points", [1, 2, 3]),
    })
    clipped = xl.clip_bbox(ds, 0, 0, 6, 6)
    assert len(clipped.points) == 2


def test_to_dem():
    ds = xr.Dataset({
        "X": ("points", [0, 1, 2, 2]),
        "Y": ("points", [0, 0, 1, 1]),
        "Z": ("points", [1, 2, 3, 4]),
    })
    dem = xl.to_dem(ds, resolution=1.0)
    assert dem.shape == (2, 3)
    assert not np.isnan(dem).all()


@pytest.mark.skipif(xl.pdal is None, reason="pdal not installed")
def test_read_las_to_xarray():
    sample_las_file = "../sample_data/0368.las"
    ds = xl.read_las_to_xarray(sample_las_file)
    assert isinstance(ds, xr.Dataset)
    assert "X" in ds


def test_clip_polygon():
    ds = xr.Dataset({
        "X": ("points", [0, 5, 10]),
        "Y": ("points", [0, 5, 10]),
    })
    poly = Polygon([(0, 0), (0, 6), (6, 6), (6, 0)])
    clipped = xl.clip_polygon(ds, poly)
    assert len(clipped.points) == 2


def test_merge_point_clouds_and_bounds():
    ds1 = xr.Dataset({"X": ("points", [0]), "Y": ("points", [0])})
    ds2 = xr.Dataset({"X": ("points", [2]), "Y": ("points", [3])})
    merged = xl.merge_point_clouds([ds1, ds2])
    assert len(merged.points) == 2
    assert xl.get_bounds(merged) == (0.0, 0.0, 2.0, 3.0)
