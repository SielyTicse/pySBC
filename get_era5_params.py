"""
Set ERA5 user defined parameters
"""

y0 = 1951 # Initial year
y1 = 1960 # Final year

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

out_path = '/projectsa/NEMO/Forcing'
