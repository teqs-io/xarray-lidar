import pytest
from xarray_pdal import read_las_to_xarray

def test_read_las_to_xarray():
    # Provide a path to a sample .las file for testing
    sample_las_file = "../sample_data/0368.las"
    
    # Call the function
    dataset = read_las_to_xarray(sample_las_file)
    
    # Perform some basic checks
    assert isinstance(dataset, xr.Dataset)
    assert "X" in dataset
    assert "Y" in dataset
    assert "Z" in dataset
