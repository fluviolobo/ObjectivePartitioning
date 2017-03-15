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
from    timeStamp                   import  fullStamp

# _2D_plot_data
#   This function plots the 2D data sets of the specified face
def _2D_plot_data(data, state, dtype):

    scatter_format = ''
    if dtype == 'nodes':
        print fullStamp() + " 2D Plotting of " + dtype + " at state " + str(state)
        x = data['state'][state][dtype]['xcoord']
        y = data['state'][state][dtype]['ycoord']
        z = data['state'][state][dtype]['zcoord']
        scatter_format = 'b.'
    elif dtype == 'elements':
        print fullStamp() + " 2D Plotting of " + dtype + "(centroid) at state " + str(state)
        x = data['state'][state][dtype]['centroid']['xcoord']
        y = data['state'][state][dtype]['centroid']['ycoord']
        z = data['state'][state][dtype]['centroid']['zcoord']
        scatter_format = 'r.'

    _2D_fig = plt.figure()
    plt.subplot(131)
    plt.plot(x,y,scatter_format)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.subplot(132)
    plt.plot(x,z,scatter_format)
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.grid(True)

    plt.subplot(133)
    plt.plot(y,z,scatter_format)
    plt.xlabel('Y')
    plt.ylabel('Z')
    plt.grid(True)
    
    plt.show()

# _2D_plot_shape
#   This function plots the objective shape data
def _2D_plot_shape(shapes,stype):

    print fullStamp() + " 2D Plotting of " + str(shapes)
    x = shapes[stype]['surface']['xcoord']
    y = shapes[stype]['surface']['ycoord']
    z = shapes[stype]['surface']['zcoord']
    scatter_format = 'b.'

    _2D_fig = plt.figure()
    plt.subplot(131)
    plt.plot(x,y,scatter_format)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.subplot(132)
    plt.plot(x,z,scatter_format)
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.grid(True)

    plt.subplot(133)
    plt.plot(y,z,scatter_format)
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
def _2D_face_slider(data, face, dtype):

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    initial_state = data['state']['number'][0]                                      # initial data set state
    final_state   = data['state']['number'][len(data['state']['number'])-1]         # final data set state
    print final_state

    scatter_format = ''
    if dtype == 'nodes':
        x = data['state'][str(initial_state)][dtype]['xcoord']                          # pulling the initial data array for x
        y = data['state'][str(initial_state)][dtype]['ycoord']                          # ...y
        z = data['state'][str(initial_state)][dtype]['zcoord']                          # ...z

        min_x = min( data['state'][str(initial_state)][dtype]['xcoord'] )               # finding the min value of x in the set, for scaling
        max_x = max( data['state'][str(final_state)][dtype]['xcoord'] )                 # finding the max value of x in the set, for scaling
        min_y = min( data['state'][str(initial_state)][dtype]['ycoord'] )               # ...y
        max_y = max( data['state'][str(final_state)][dtype]['ycoord'] )                 # ...y
        min_z = min( data['state'][str(initial_state)][dtype]['zcoord'] )               # ...z
        max_z = max( data['state'][str(final_state)][dtype]['zcoord'] )                 # ...z

        scatter_format = 'b.'
        
    elif dtype == 'elements':
        x = data['state'][str(initial_state)][dtype]['centroid']['xcoord']                          # pulling the initial data array for x
        y = data['state'][str(initial_state)][dtype]['centroid']['ycoord']                          # ...y
        z = data['state'][str(initial_state)][dtype]['centroid']['zcoord']                          # ...z

        min_x = min( data['state'][str(initial_state)][dtype]['centroid']['xcoord'] )               # finding the min value of x in the set, for scaling
        max_x = max( data['state'][str(final_state)][dtype]['centroid']['xcoord'] )                 # finding the max value of x in the set, for scaling
        min_y = min( data['state'][str(initial_state)][dtype]['centroid']['ycoord'] )               # ...y
        max_y = max( data['state'][str(final_state)][dtype]['centroid']['ycoord'] )                 # ...y
        min_z = min( data['state'][str(initial_state)][dtype]['centroid']['zcoord'] )               # ...z
        max_z = max( data['state'][str(final_state)][dtype]['centroid']['zcoord'] )                 # ...z

        scatter_format = 'r.'
    
    if face == 'xy' or face == 'yx':
        l, = plt.plot(x, y, scatter_format)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis( [(min_x*0.90), (max_x*1.10), (min_y*0.90), (max_y*1.10)] )
    elif face == 'xz' or face == 'zx':
        l, = plt.plot(x, z, scatter_format)
        plt.xlabel('X')
        plt.ylabel('Z')
        plt.axis( [(min_x*0.90), (max_x*1.10), (min_z*0.90), (max_z*1.10)] )
    elif face == 'yz' or face == 'zy':
        l, = plt.plot(y, z, scatter_format)
        plt.xlabel('Y')
        plt.ylabel('Z')
        plt.axis( [(min_y*0.90), (max_y*1.10), (min_z*0.90), (max_z*1.10)] )

    plt.grid(True)

    axcolor = 'lightgoldenrodyellow'
    ax_state = plt.axes([0.10, 0.10, 0.80, 0.05], facecolor=axcolor)
    slider_state = Slider(ax_state, 'State', initial_state, final_state, valinit=initial_state, valfmt='%3d')

    def update(val):
        current_state_val = slider_state.val
        truncated_state_val = int(m.floor(current_state_val))
        #print str(current_state_val) + "," + str(truncated_state_val)
        if current_state_val >= truncated_state_val and current_state_val < (truncated_state_val+1):
            if dtype == 'nodes':
                if face == 'xy' or face == 'yx':
                    l.set_xdata( data['state'][str(truncated_state_val)][dtype]['centroid']['xcoord'] )
                    l.set_ydata( data['state'][str(truncated_state_val)][dtype]['centroid']['ycoord'] )
                elif face == 'xz' or face == 'zx':
                    l.set_xdata( data['state'][str(truncated_state_val)][dtype]['centroid']['xcoord'] )
                    l.set_ydata( data['state'][str(truncated_state_val)][dtype]['centroid']['zcoord'] )
                elif face == 'yz' or face == 'zy':
                    l.set_xdata( data['state'][str(truncated_state_val)][dtype]['centroid']['ycoord'] )
                    l.set_ydata( data['state'][str(truncated_state_val)][dtype]['centroid']['zcoord'] )
            elif dtype == 'elements':
                if face == 'xy' or face == 'yx':
                    l.set_xdata( data['state'][str(truncated_state_val)][dtype]['centroid']['xcoord'] )
                    l.set_ydata( data['state'][str(truncated_state_val)][dtype]['centroid']['ycoord'] )
                elif face == 'xz' or face == 'zx':
                    l.set_xdata( data['state'][str(truncated_state_val)][dtype]['centroid']['xcoord'] )
                    l.set_ydata( data['state'][str(truncated_state_val)][dtype]['centroid']['zcoord'] )
                elif face == 'yz' or face == 'zy':
                    l.set_xdata( data['state'][str(truncated_state_val)][dtype]['centroid']['ycoord'] )
                    l.set_ydata( data['state'][str(truncated_state_val)][dtype]['centroid']['zcoord'] )

        fig.canvas.draw()

    slider_state.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    def reset(event):
        slider_state.reset()

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

# _3D_plot_shape
#   This function plots the shape data sets in 3D
def _3D_plot_shape(shapes, stype):

    x = shapes[stype]['surface']['xcoord']
    y = shapes[stype]['surface']['ycoord']
    z = shapes[stype]['surface']['zcoord']
    
    _3D_fig = plt.figure()
    plt3 = _3D_fig.add_subplot(111, projection='3d')
    plt3.scatter(x,y,z)
    plt3.set_xlabel('X Label')
    plt3.set_ylabel('Y Label')
    plt3.set_zlabel('Z Label')
    plt.show()
