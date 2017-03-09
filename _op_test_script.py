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
_2D_plot_data(data, '559', 'nodes')

# 2D plot data face
_2D_plot_face(data, '1', 'nodes', 'yx')

#_2D_face_slider(data, 'nodes')

# 3D plot data
#_3D_plot_data(data, '1', 'nodes')


#
#
#
dtype = 'nodes'

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

initial_state = data['state']['number'][0]                                      # initial data set state
final_state   = data['state']['number'][len(data['state']['number'])-1]         # final data set state

x = data['state'][str(initial_state)][dtype]['xcoord']
y = data['state'][str(initial_state)][dtype]['ycoord']
#z = data['state'][state][dtype]['zcoord']

l, = plt.plot(x, y, 'b.')

axcolor = 'lightgoldenrodyellow'
ax_state = plt.axes([0.10, 0.1, 0.65, 0.03], facecolor=axcolor)
slider_state = Slider(ax_state, 'State', initial_state, final_state, valinit=initial_state)

def update(val):
    current_state_val = slider_state.val
    truncated_state_val = int(m.floor(current_state_val))
    print str(current_state_val) + "," + str(truncated_state_val)
    if current_state_val >= truncated_state_val and current_state_val < (truncated_state_val+1):
        l.set_xdata( data['state'][str(truncated_state_val)][dtype]['xcoord'] )
        l.set_ydata( data['state'][str(truncated_state_val)][dtype]['ycoord'] )

    fig.canvas.draw_idle()

slider_state.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    slider_state.reset()

button.on_clicked(reset)

plt.show()
