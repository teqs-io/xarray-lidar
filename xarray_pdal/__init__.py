import pdal
import xarray as xr
import numpy as np

def read_las_to_xarray(las_file_path):
    """
    Reads a .las file using PDAL and converts it to an xarray Dataset.

    Parameters:
    las_file_path (str): Path to the .las file.

    Returns:
    xarray.Dataset: The converted xarray Dataset.
    """
    pipeline = pdal.Pipeline(f"""
    {{
        "pipeline": [
            "{las_file_path}"
        ]
    }}
    """)
    pipeline.execute()
    arrays = pipeline.arrays[0]

    data_vars = {key: (["points"], np.array(value)) for key, value in arrays.items()}
    coords = {"points": np.arange(len(arrays["X"]))}

    return xr.Dataset(data_vars, coords)
