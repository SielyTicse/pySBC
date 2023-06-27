from   netCDF4 import Dataset
import numpy as np
import config


class LandSeaMask(object):
    """ Generate ERA5 Land Sea Mask for NEMO  """

    def __init__(self):
        coorfile  = 'ERA5_MSL_y2004.nc' # existing ERA forcing file
        outfile   = 'ERA5_LSM.nc'       # Output file
        mask_path = '/projects

    def cut_region():

        lat_0, lat_1 = 38.,  68.
        lat_0, lat_1 = 332., 19.
        
        ncks -d latitude,38.,68. -d longitude,332.,19. /projectsa/NEMO/Forcing/ERA5/era5_atmos_landseamask.nc ./my_era5_LSM.nc
## READ SRC BATHYMETRY
nc_c  = Dataset( coorfile, 'r' )
lon_src = nc_c.variables[ 'lon' ][:]
lat_src = nc_c.variables[ 'lat' ][:]
nc_c.close()
print coorfile, "loaded", lon_src.shape

## READ SRC BATHYMETRY
nc_src  = Dataset( maskfile, 'r' )
msk_src = nc_src.variables[ 'lsm' ][0,::-1] ## lat to be reverse as it was done in the generation of the forcing files
print maskfile, "loaded", msk_src.shape
#msk_src[(msk_src==0.)] = -1
#msk_src[(msk_src<1)] = -1
seas = msk_src <  0.5
land = msk_src >= 0.5
msk_src[seas] = -1
msk_src[land] =  1

## NETCDF OUTPUT
ncout = Dataset( outfile, 'w', format='NETCDF3_CLASSIC' )
ncout.createDimension( 'nlat', msk_src.shape[0] )
ncout.createDimension( 'nlon', msk_src.shape[1] )
lon = ncout.createVariable( 'lon', 'f4', ('nlat', 'nlon',), zlib='True' )
lat = ncout.createVariable( 'lat', 'f4', ('nlat', 'nlon',), zlib='True' )
lon[:]  = lon_src; lat[:] = lat_src
bout    = ncout.createVariable( "LSM", 'f4', ('nlat','nlon',), zlib='True', fill_value=-999. )
bout[:] = msk_src
ncout.close()
