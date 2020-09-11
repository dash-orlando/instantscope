'''
vtk2line

    Utility for the InstantScope App
        - Extracts point coordinates from "line model" VTK file
        - Stores point coordinates in CSV file

Fluvio L Lobo Fenoglietto
Madelene Habib
09-11-2020
'''

# IMPORT MODULES ---------------------------------------------------------- #
import  os
import  tkinter     as tk
import  numpy       as np
from    tkinter     import filedialog

# PROGRAM ----------------------------------------------------------------- #
root = tk.Tk()                                                              # create TK object
root.withdraw()

vtkfile = filedialog.askopenfilename()                                      # define input VTK file from browser window
logfile = os.path.splitext(vtkfile)[0]+'.csv'                               # define output CSV file

print( 'Input  VTK file = {}'.format( vtkfile ) )                           # print input and output filenames
print( 'Output CSV file = {}'.format( logfile ) )                           # ...

with open( vtkfile ) as infile:

    i = 0                                                                   # here we initialize a counter
    point_label_flag = 0                                                    # here we create a variable that works as a binary flag
    points = []
    
    for line in infile:
        line = (' '.join((line.strip('\n')).split())).split(' ')
        
        if line[0] == 'POINTS':                                             # here we print the value of the counter when we find the label points
            point_label_flag = 1                                            # here we flip the value of the flag to 1, which marks the beginning of the POINTS section
        
        elif point_label_flag == 1:                                         # and then here we can just check for the state of this flag

            if len(line) == 9:
                points.append( '{},{},{}'.format(line[0], line[1], line[2]) )
                points.append( '{},{},{}'.format(line[3], line[4], line[5]) )
                points.append( '{},{},{}'.format(line[6], line[7], line[8]) )
            if len(line) == 6:
                points.append( '{},{},{}'.format(line[0], line[1], line[2]) )
                points.append( '{},{},{}'.format(line[3], line[4], line[5]) )
            if len(line) == 3:
                points.append( '{},{},{}'.format(line[0], line[1], line[2]) )
            
        if line[0] == 'METADATA':
            break

        i = i + 1

# done with loop --------------------------------- #
points = points[:-1]

with open( logfile, "w+" ) as outfile:
    for line in points:
        outfile.write(line)
        outfile.write('\n')

