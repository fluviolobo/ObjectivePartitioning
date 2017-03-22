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
def _sphere_shape(R,x0,y0,z0,res):
    
    print fullStamp() + " Generating Shape"

    shapes = {}
    shapes['sphere'] = {}
    shapes['sphere']['R'] = R
    shapes['sphere']['origin'] = {}
    shapes['sphere']['origin']['x0'] = x0
    shapes['sphere']['origin']['y0'] = y0
    shapes['sphere']['origin']['z0'] = z0
    shapes['sphere']['surface'] = {}
    shapes['sphere']['surface']['theta'] = {}
    shapes['sphere']['surface']['phi'] = {}
    
    # generating radian and degree arrays
    theta_rads = np.linspace(0, np.pi, res)
    theta_degrees = theta_rads*(180/np.pi)
    shapes['sphere']['surface']['theta']['rads'] = theta_rads
    shapes['sphere']['surface']['theta']['degrees'] = theta_degrees

    phi_rads = np.linspace(-np.pi, np.pi, res)
    phi_degrees = phi_rads*(180/np.pi)
    shapes['sphere']['surface']['phi']['rads'] = phi_rads
    shapes['sphere']['surface']['phi']['degrees'] = phi_degrees

    # calculating cartesian coordinates
    N_rads = len(theta_rads)
    x = []
    y = []
    z = []
    for i in range(0, N_rads):
        for j in range(0, N_rads):
            x.append( R*np.sin(theta_rads[i])*np.cos(phi_rads[j]) )
            y.append( R*np.sin(theta_rads[i])*np.sin(phi_rads[j]) )
            z.append( R*np.cos(theta_rads[i]) )

    shapes['sphere']['surface']['xcoord'] = x
    shapes['sphere']['surface']['ycoord'] = y
    shapes['sphere']['surface']['zcoord'] = z
    
    return shapes
