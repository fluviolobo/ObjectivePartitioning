"""
    Objective Partitioning
    --Functions Module

    Fluvio L Lobo Fenoglietto
    03/06/2017
"""

import Tkinter
import tkFileDialog

# _browse_data_file
#   This function allows the user to browse and select the data file to be analyze
def _browse_data_file():
    root = Tkinter.Tk()
    target_file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if target_file != None:
        raw_data = target_file.read()
        target_file.close()
        #print "I got %d bytes from this file." % len(data)
    root.destroy()
    return target_file, raw_data
