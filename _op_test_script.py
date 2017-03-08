"""
    Objective Partitioning
    --Test Script

    Fluvio L Lobo Fenoglietto
    03/06/2017
"""

from _op_functions_module import _browse_data_file
from _op_functions_module import _parse_data
from _op_functions_module import _3D_plot_data

import  matplotlib.pyplot           as      plt
from    mpl_toolkits.mplot3d        import  Axes3D

# browse data file
target_file, file_path, file_dir, file_name, raw_data = _browse_data_file()

# split raw daat into lines

data = _parse_data(file_name, raw_data)

# 3D plot data
_3D_plot_data(data, '1', 'nodes')
