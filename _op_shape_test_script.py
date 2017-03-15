"""
    Objective Partitioning
    --Test Script

    Fluvio L Lobo Fenoglietto
    03/14/2017
"""
import  numpy                       as      np
import  math                        as      m
import  matplotlib.pyplot           as      plt
from    matplotlib.widgets          import  Slider, Button, RadioButtons
from    mpl_toolkits.mplot3d        import  Axes3D

from timeStamp                      import *

from _op_parsing_functions          import _browse_data_file
from _op_parsing_functions          import _parse_data
from _op_processing_functions       import _centroid_calc
from _op_shape_functions            import _sphere_shape
from _op_visualization_functions    import _2D_plot_shape
from _op_visualization_functions    import _3D_plot_shape

# create shape --sphere
x0 = 0
y0 = 0
z0 = 0
R = 10
res = 20
shapes = _sphere_shape(R,x0,y0,z0,res)

_2D_plot_shape(shapes,'sphere')

_3D_plot_shape(shapes, 'sphere')
