"""
    Objective Partitioning
    --Test Script

    Fluvio L Lobo Fenoglietto
    03/06/2017
"""
import  numpy                       as      np
import  math                        as      m
import  matplotlib.pyplot           as      plt
from    matplotlib.widgets          import  Slider, Button, RadioButtons
from    mpl_toolkits.mplot3d        import  Axes3D


from _op_functions_module           import _browse_data_file
from _op_functions_module           import _parse_data
from _op_visualization_functions    import _2D_plot_data
from _op_visualization_functions    import _2D_plot_face
from _op_visualization_functions    import _2D_face_slider
from _op_visualization_functions    import _3D_plot_data

# browse data file
target_file, file_path, file_dir, file_name, raw_data = _browse_data_file()

# split raw daat into lines

data = _parse_data(file_name, raw_data)

# 2D plot data
_2D_plot_data(data, '3', 'nodes')

# 2D plot data face
_2D_plot_face(data, '1', 'nodes', 'yx')

_2D_face_slider(data, 'nodes')

# 3D plot data
#_3D_plot_data(data, '1', 'nodes')




