"""
    Objective Partitioning
    --Visualization Module

    Fluvio L Lobo Fenoglietto
    03/09/2017
"""

# imports
import  numpy                       as      np
import  math                        as      m
import  matplotlib.pyplot           as      plt
from    matplotlib.widgets          import  Slider, Button, RadioButtons
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

# _2D_face_slider
#   This function plots the data of a specific face from the entire data set
#   The state of the data to be plotted is chosen through a slider
def _2D_face_slider(data, dtype):

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    x = data['state'][state][dtype]['xcoord']
    y = data['state'][state][dtype]['ycoord']
    #z = data['state'][state][dtype]['zcoord']

    l, = plt.plot(x, y, 'b.')

    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.10, 0.1, 0.65, 0.03], facecolor=axcolor)
    sfreq = Slider(axfreq, 'Freq', 1, 3, valinit=1)

    def update(val):
        freq = sfreq.val
        truncated = int(m.floor(freq))
        print str(freq) + "," + str(truncated)
        if freq >= truncated and freq < (truncated+1):
            l.set_xdata(time[str(truncated-1)])
            l.set_ydata(samp[str(truncated-1)])

        fig.canvas.draw_idle()

    sfreq.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    def reset(event):
        sfreq.reset()

    button.on_clicked(reset)

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


