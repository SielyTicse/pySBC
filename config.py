"""
Set ERA5 user defined parameters
"""

y0 = 1961 # Initial year
y1 = 1978 # Final year

# Variable list
var_list = [ '10m_u_component_of_wind',
             '10m_v_component_of_wind',
             '2m_dewpoint_temperature',
             '2m_temperature',
             'mean_sea_level_pressure',
             'mean_snowfall_rate',
             'mean_surface_downward_long_wave_radiation_flux',
             'mean_surface_downward_short_wave_radiation_flux',
             'mean_total_precipitation_rate',
             'surface_pressure', ]

head = '/projectsa/NEMO' # head path
raw_path       = head + '/NEMO/Forcing'    # raw data
tmp_path       = head + '/ryapat/Extract'  # temp extraction space
processed_path = head + '/ryapat/Forcing'  # processed forcing

# set domain extent
east  =   19.  # east border
west  =  -28.  # west border
north =   68.  # north border
south =   38.  # south border
