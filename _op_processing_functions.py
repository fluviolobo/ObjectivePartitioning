"""
    Objective Partitioning
    --Processing Functions

    This module contains functions that modify, alter or processes parsed data sets

    Fluvio L Lobo Fenoglietto
    03/10/2017
"""

from timeStamp      import fullStamp

# _centroid_calc
#   This function calculates the centroid of the elements that compose a mesh
#   Why do we calculate centroids?
#       Centroids are used to better determine the elements that fall within a region of interest
#       This calculation is more efficient than checking if a majority of an elements nodes fall within a region of interest
#       Centroids can also be used for less convoluted graphing of the deformable body
def _centroid_calc(data):
    print fullStamp() + " Calculating Element Centroids"

    N_states = len(data['state']['number'])
    N_elements = len(data['state']['init']['elements']['number'])

    for h in range(0, N_states+1):

        if h == 0:

            state = 'init'
            print fullStamp() + " Calculating Centroids for State " + state

        elif h > 0:

            state = str(data['state']['number'][h-1])
            print fullStamp() + " Calculating Centroids for State " + state
    
        data['state'][state]['elements']['centroid'] = {}
        data['state'][state]['elements']['centroid']['xcoord'] = []
        data['state'][state]['elements']['centroid']['ycoord'] = []
        data['state'][state]['elements']['centroid']['zcoord'] = []

        for i in range(0, N_elements):

            ele_num = data['state']['init']['elements']['number'][i]
            #print fullStamp() + " Element Number = " + str(ele_num)
            ele_nodes = data['state']['init']['elements']['connectivity'][i]
            #print fullStamp() + " Element Nodes = " + str(ele_nodes)
            N_element_nodes = len(data['state']['init']['elements']['connectivity'][i])
            #print fullStamp() + " Nodes per Element = " + str(N_element_nodes)

            x_coord_sum = 0.0
            y_coord_sum = 0.0
            z_coord_sum = 0.0
            for j in range(0, N_element_nodes):

                selected_ele_node = data['state']['init']['elements']['connectivity'][i][j]
                #print fullStamp() + " Selected Node = " + str(selected_ele_node)

                N_nodes = len(data['state']['init']['nodes']['number'])

                x_coord_sum += data['state'][state]['nodes']['xcoord'][selected_ele_node-1]
                #print fullStamp() + " X Sum = " + str(x_coord_sum)
                y_coord_sum += data['state'][state]['nodes']['ycoord'][selected_ele_node-1]
                #print fullStamp() + " Y Sum = " + str(y_coord_sum)
                z_coord_sum += data['state'][state]['nodes']['zcoord'][selected_ele_node-1]
                #print fullStamp() + " Z Sum = " + str(z_coord_sum)

                """
                for k in range(0, N_nodes):

                    node = data['state']['init']['nodes']['number'][k]
                    #print node
                    
                    if selected_ele_node == node:

                        x_coord_sum += data['state'][state]['nodes']['xcoord'][k]
                        #print fullStamp() + " X Sum = " + str(x_coord_sum)
                        y_coord_sum += data['state'][state]['nodes']['ycoord'][k]
                        #print fullStamp() + " Y Sum = " + str(y_coord_sum)
                        z_coord_sum += data['state'][state]['nodes']['zcoord'][k]
                        #print fullStamp() + " Z Sum = " + str(z_coord_sum)
                """
                
            #print fullStamp() + " X Centroid = " + str(x_coord_sum/N_element_nodes)
            #print fullStamp() + " Y Centroid = " + str(y_coord_sum/N_element_nodes)
            #print fullStamp() + " Z Centroid = " + str(z_coord_sum/N_element_nodes)
            data['state'][state]['elements']['centroid']['xcoord'].append(x_coord_sum/N_element_nodes)
            data['state'][state]['elements']['centroid']['ycoord'].append(y_coord_sum/N_element_nodes)
            data['state'][state]['elements']['centroid']['zcoord'].append(z_coord_sum/N_element_nodes)

    return data
