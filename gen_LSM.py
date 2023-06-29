import xarray as xr
import config
import os

class LandSeaMask(object):
    """ Generate ERA5 Land Sea Mask for NEMO  """

    def __init__(self):
        # set paths
        self.tmp_path    = config.tmp_path
        self.global_mask = config.raw_path + '/ERA5/era5_atmos_landseamask.nc' 

        self.cut_off = 0.5  # flooding cell fraction

        # domain extent
        self.east = config.east
        self.west = config.west
        self.north = config.north
        self.south = config.south

        # assert 0-360 lon format
        self.assert_lons()

    def assert_lons(self):
        """
        Ensure requested longitudes are in 0-360 format
        """

        # conform longitude format
        if self.west < 0 : self.west = 360. + self.west
        if self.east < 0 : self.east = 360. + self.east

    def cut_region_ncks(self):
        """
        Cut source Land Sea Mask to domain
        """


        # extracted output path
        self.extracted_path = config.processed_path + \
                              '/ERA5_LSM_{0}_{1}_{2}_{3}.nc'.format(
                              self.west, self.east, self.south, self.north)

        # set ncks
        cmd_str = "ncks -d latitude,{0},{1} -d longitude,{2},{3} {4} {5}"

        # format ncks
        cmd = cmd_str.format(self.south, self.north, self.west, self.east,
                             self.global_mask, self.extracted_path)
        print (cmd)
        
        # exectute ncks
        os.system( cmd )

    def cut_region_python(self):
        """
        Cut source Land Sea Mask to domain
        
        ***Under construction***
        Pythonic replacement for ncks to reduce number of files created.
        """

        # open extracted mask
        msk = xr.open_dataarray(self.global_mask)

        # extract region
        msk = msk.where((msk.longitude > self.west) &
                        (msk.longitude < self.east) &
                        (msk.latitude > self.south) &
                        (msk.latitude < self.north), drop=True)

        msk.to_netcdf(config.processed_path + '/ERA5_LSM_python.nc') 
 
    def cut_method_compare(self):
        """
        Temporary function to compare extraction methods.
        """

        msk_python = xr.open_dataarray(
                          config.processed_path + '/ERA5_LSM_python.nc') 
        msk =  xr.open_dataarray(config.processed_path + '/ERA5_LSM.nc') 

        print (msk)
        print (msk_python)

if __name__ == '__main__':
    LSM = LandSeaMask()
    LSM.cut_region_ncks()
