from setuptools import setup, find_packages

setup(
    name='xarray-pdal',
    version='0.0.0',
    author='Taimur Khan',
    author_email='taimur.khan@ufz.de',
    description='A package for working with point cloud data in xarray using PDAL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/xarray-pdal',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pdal',
        'xarray',
        'numpy',
    ],
)
