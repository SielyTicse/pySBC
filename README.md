# pySBC

Scripts for generating surface boundary conditions for regional NEMO 
configurations.

 - gen_era5.py: Based on a script of Nico's, which processes ERA5 data
   ready for use with NEMO. The reference parameter choices are for AMM15.
 - gen_era5_legacy.py: Nico's original script.

### Setup - conda environment
Use the following to configure a conda environment for use with pySBC.
~~~
conda env create -f environment.yml
~~~
