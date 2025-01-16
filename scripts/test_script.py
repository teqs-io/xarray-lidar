from xarray_pdal import read_las_to_xarray

# Replace 'path/to/sample.las' with the actual path to your sample .las file
sample_las_file = '../sample_data/0368.las'

# Call the function and print the result
dataset = read_las_to_xarray(sample_las_file)
print(dataset)
