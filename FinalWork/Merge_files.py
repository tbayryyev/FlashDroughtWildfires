import glob
import netCDF4 as nc
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# combines all the netcdf files into 1 file 
# searches for all netcdf files in the directory and then combines them into 1 netcdf file called 'Data.nc'
ds = xr.open_mfdataset('*.nc4')
ds.to_netcdf('Data.nc')
