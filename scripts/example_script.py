from xarray_lidar import read_point_cloud

# Replace 'path/to/sample.las' with the actual path to your sample .las file
sample_las_file = '../sample_data/0368.las'

# Call the function and print the result
dataset = read_point_cloud(sample_las_file)
print(dataset)
