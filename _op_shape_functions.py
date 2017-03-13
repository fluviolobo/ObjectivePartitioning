"""
    Objective Partitioning
    --Shapes

    This module contains the functions related to the shapes used to outline a region of interest within a mesh

    Fluvio L Lobo Fenoglietto
    03/12/2017
"""

import  numpy       as      np
from    timeStamp   import  fullStamp

# define sphere
def _sphere_shape(R,x0,y0,z0):
    
    print fullStamp() + " Generating Shape"

    shapes = {}
    shapes['sphere'] = {}
    shapes['sphere']['R'] = R
    shapes['sphere']['origin'] = R
    
    # generating radian and degree arrays
    theta_rads = np.linspace(-np.pi, np.pi, 200)
    theta_degrees = rads*(180/np.pi)

    phi_rads = np.linspace(-np.pi, np.pi, 200)
    phi_degrees = rads*(180/np.pi)

    # calculating cartesian coordinates
    

    return rads, degrees
