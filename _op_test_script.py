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


