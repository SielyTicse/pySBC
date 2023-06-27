import xarray as xr
import config
import os

class LandSeaMask(object):
    """ Generate ERA5 Land Sea Mask for NEMO  """

    def __init__(self):
        # set paths
        self.tmp_path = config.tmp_path
        self.mask_in  = config.raw_path + '/ERA5/era5_atmos_landseamask.nc' 
        self.out_path = config.processed_path 

        self.cut_off = 0.5  # flooding cell fraction

        # domain extent
        self.east = config.east
        self.west = config.west
        self.north = config.north
        self.south = config.south

    def cut_region(self):
        """
        Cut source Land Sea Mask to domain
        """

        # conform longitude format
        if self.west < 0 : self.west = 360. + self.west
        if self.east < 0 : self.east = 360. + self.east

        # output path
        fout = self.out_path + '/ERA5_LSM_{0}_{1}_{2}_{3}.nc'.format(
                self.west, self.east, self.south, self.north)

        # set ncks
        cmd_str = "ncks -d latitude,{0},{1} -d longitude,{2},{3} {4} {5}"

        # format ncks
        cmd = cmd_str.format(self.west, self.east, self.south, self.north,
                             self.mask_in, fout)
        print (cmd)
        
        # exectute ncks
        os.system( cmd )

    def assert_binary_mask(self):
        """
        Set mask to be -1 (sea) or 1 (land).
        """

        # load
        msk = xr.open_dataarray(self.mask_in)

        # assert binary mask (from R+)
        msk = xr.where(msk  <  self.cut_off, -1, 1)

        # save
        msk.to_netcdf(self.out_path + '/ERA5_LSM.nc') 

if __name__ == '__main__':
    LSM = LandSeaMask()
    LSM.cut_region()
    LSM.assert_binary_mask()
