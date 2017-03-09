"""
    Objective Partitioning
    --Functions Module

    Fluvio L Lobo Fenoglietto
    03/06/2017
"""

import  Tkinter
import  tkFileDialog
import  matplotlib.pyplot           as      plt
from    mpl_toolkits.mplot3d        import  Axes3D

# _browse_data_file
#   This function allows the user to browse and select the data file to be analyze
def _browse_data_file():
    root = Tkinter.Tk()
    target_file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if target_file != None:
        raw_data = target_file.read()
        target_file.close()

    # determining path of the file
    file_path = str(target_file.name)

    # determining the directory of the file
    split_file_path = file_path.split("/")
    file_dir = ""
    for i in range(0, len(split_file_path)-1):
        file_dir += split_file_path[i] + "/"

    # determining the file name
    file_name = split_file_path[len(split_file_path)-1]

    root.destroy()
    return target_file, file_path, file_dir, file_name, raw_data


# _parse_data()
#   This function reads the PostView ASCii data exports and separates nodal and element data in a python dictionary
def _parse_data(data_name, raw_data):

    data = {}
    data['state'] = {}
    data['state']['number'] = []

    state_flag = 0
    nodes_flag = 0
    elements_flag = 0
    line_data = raw_data.split('\n')
    num_lines = len(line_data)
    for i in range(0, num_lines):

        # nodal data collection
        if nodes_flag == 1:
            split_data = line_data[i].split(',')
            if len(split_data) > 1:
                data['state'][state]['nodes']['number'].append(float(split_data[0]))
                data['state'][state]['nodes']['xcoord'].append(float(split_data[1]))
                data['state'][state]['nodes']['ycoord'].append(float(split_data[2]))
                data['state'][state]['nodes']['zcoord'].append(float(split_data[3][:-1]))
            else:
                pass

        # element data collection
        elif elements_flag == 1:
            split_data = line_data[i].split(',')
            if len(split_data) > 1:
                data['state'][state]['elements']['number'].append(float(split_data[0]))
                data['state'][state]['elements'][data_name].append(float(split_data[1][:-1]))
            else:
                pass
            
        # identifying data file sections
        # state
        if line_data[i][0:6] == "*STATE":
            state_flag = 1
            state = line_data[i][7:-1]
            print "STATE " + state + " Found"
            data['state']['number'].append(int(state))
            data['state'][state] = {}
        # time
        elif line_data[i][0:11] == "*TIME_VALUE":
            time_value = line_data[i][12:-1]
            print "TIME_VALUE " + time_value
            data['state'][state]['time'] = time_value
        # nodal data
        elif line_data[i][0:6] == "*NODES" and state_flag == 1:
            nodes_flag = 1
            elements_flag = 0
            data['state'][state]['nodes'] = {}
            data['state'][state]['nodes']['number'] = []
            data['state'][state]['nodes']['xcoord'] = []
            data['state'][state]['nodes']['ycoord'] = []
            data['state'][state]['nodes']['zcoord'] = []
        # element data   
        elif line_data[i][0:13] == "*ELEMENT_DATA":
            nodes_flag = 0
            elements_flag = 1
            data['state'][state]['elements'] = {}
            data['state'][state]['elements']['number'] = []
            data['state'][state]['elements'][data_name] = []

    return data

# end of _parse_data()
