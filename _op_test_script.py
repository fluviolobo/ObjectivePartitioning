"""
    Objective Partitioning
    --Test Script

    Fluvio L Lobo Fenoglietto
    03/06/2017
"""

from _op_functions_module import _browse_data_file

# browse data file
target_file, raw_data = _browse_data_file()

# split raw daat into lines
line_data = raw_data.split('\n')

# using dictionaries
data = {}
data['state'] = {}

# find all states and subsequent data
state_flag = 0
nodes_flag = 0
elements_flag = 0
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
    
    elif elements_flag == 1:
        split_data = line_data[i].split(',')
        if len(split_data) > 1:
            data['state'][state]['elements']['number'].append(float(split_data[0]))
            data['state'][state]['elements']['value'].append(float(split_data[1][:-1]))
        else:
            pass
        
    
    if line_data[i][0:6] == "*STATE":
        state_flag = 1
        state = line_data[i][7:-1]
        print "STATE " + state + " Found"
        data['state'][state] = {}
    # Adding time
    elif line_data[i][0:11] == "*TIME_VALUE":
        time_value = line_data[i][12:-1]
        print "TIME_VALUE " + time_value
        data['state'][state]['time'] = time_value
    # Adding nodal values
    elif line_data[i][0:6] == "*NODES" and state_flag == 1:
        nodes_flag = 1
        elements_flag = 0
        data['state'][state]['nodes'] = {}
        data['state'][state]['nodes']['number'] = []
        data['state'][state]['nodes']['xcoord'] = []
        data['state'][state]['nodes']['ycoord'] = []
        data['state'][state]['nodes']['zcoord'] = []
        
    elif line_data[i][0:13] == "*ELEMENT_DATA":
        nodes_flag = 0
        elements_flag = 1
        data['state'][state]['elements'] = {}
        data['state'][state]['elements']['number'] = []
        data['state'][state]['elements']['value'] = []

"""
# find nodes
## find where the nodes section starts
Nlines = len(line_data)
nodes_start_indeces = []
for i in range(0, Nlines):
    if line_data[i][:-1] == "*NODES":
        print "found"
        nodes_start_indeces.append(i+1)

## find where the elements section starts
elements_start_indeces = []
for i in range(0, Nlines):
    if line_data[i][:-1] == "*ELEMENTS":
        print "found"
        elements_start_indeces.append(i)

## find where the nodes sections end, using the initial elements
Nindeces = len(nodes_start_indeces)
nodes_stop_indeces = []
for i in range(0, Nindeces):
    if i == 0:
        nodes_stop_indeces.append(elements_start_indeces[i]-1)
    else:
        nodes_stop_indeces.append(nodes_start_indeces[i]+nodes_stop_indeces[0]-2)
"""

