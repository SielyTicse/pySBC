from   netCDF4 import Dataset
import numpy as np
import config
import os

class LandSeaMask(object):
    """ Generate ERA5 Land Sea Mask for NEMO  """

    def __init__(self):
        self.mask_in = outpath + 'ERA5/era5_atmos_landseamask.nc' # LSM source
        self.out_path = '/projectsa/NEMO/ryapat/Forcing' # save path

        cut_off = 0.5  # flooding cell fraction

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
        fout = 'LandSeaMask/era5_LSM_{0}_{1}_{2}_{3}.nc'.format(
                    self.west, self.east, self.south, self.north)

        # set ncks
        cmd_str = "ncks -d latitude,{0},{1} -d longitude,{2},{3} {4} {5}"

        # format ncks
        cmd = cmd_str.format(self.west, self.east, self.south, self.north,
                             self.mask_in, fout)

        # exectute ncks
        os.system( command )

    def assert_binary_mask(self):
        """
        Set mask to be -1 (sea) or 1 (land).
        """

        # load
        msk_src = xr.open_dataset(self.mask_in)

        # assert binary mask (from R+)
        seas = msk <  cut_off
        land = msk >= cut_off
        msk[msk < cut_off] = -1
        msk[msk >= cutoff] =  1

        # save
        msk.to_netcdf(self.out_path + '/ERA5_LSM.nc') 
