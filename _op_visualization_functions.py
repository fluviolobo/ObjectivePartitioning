"""
    Objective Partitioning
    --Visualization Module

    Fluvio L Lobo Fenoglietto
    03/09/2017
"""

# imports
import  matplotlib.pyplot           as      plt
from    mpl_toolkits.mplot3d        import  Axes3D


# _2D_plot_data
#   This function plots the 2D data sets of the specified face
def _2D_plot_data(data, state, dtype):
    x = data['state'][state][dtype]['xcoord']
    y = data['state'][state][dtype]['ycoord']
    z = data['state'][state][dtype]['zcoord']

    _2D_fig = plt.figure()
    plt.subplot(131)
    plt.plot(x,y,'b.')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.subplot(132)
    plt.plot(x,z,'b.')
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.grid(True)

    plt.subplot(133)
    plt.plot(y,z,'b.')
    plt.xlabel('Y')
    plt.ylabel('Z')
    plt.grid(True)
    
    plt.show()

# _2D_plot_face
#   This function plots only the data of a specific face of the data set
def _2D_plot_face(data, state, dtype, face):
    x = data['state'][state][dtype]['xcoord']
    y = data['state'][state][dtype]['ycoord']
    z = data['state'][state][dtype]['zcoord']

    _2D_fig = plt.figure()

    if face == 'xy' or 'yx':
        plt.plot(x,y,'b.')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
    elif face == 'xz' or 'zx':
        plt.plot(x,z,'b.')
        plt.xlabel('X')
        plt.ylabel('Z')
        plt.grid(True)
    elif face == 'yz' or 'zy':
        plt.plot(y,z,'b.')
        plt.xlabel('Y')
        plt.ylabel('Z')
        plt.grid(True)
    
    plt.show()

# _3D_plot_data
#   This function plots the data sets with given input parameters
def _3D_plot_data(data, state, dtype):
    x = data['state'][state][dtype]['xcoord']
    y = data['state'][state][dtype]['ycoord']
    z = data['state'][state][dtype]['zcoord']

    _3D_fig = plt.figure()
    plt3 = _3D_fig.add_subplot(111, projection='3d')
    plt3.scatter(x,y,z)
    plt3.set_xlabel('X Label')
    plt3.set_ylabel('Y Label')
    plt3.set_zlabel('Z Label')
    plt.show()


