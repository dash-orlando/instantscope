'''
Instant Scope :: GUI

    This script creates a user interface that allows
    user to input the patient's information with the
    goal of ganerating a patient-specific
    laryngoscope design.

Madelene Habib
Fluvio L Lobo Fenoglietto
'''

# import tkinter module
import tkinter as tk

# import internal modules
import  _instantscope    as _is
#import  _gspread         as _gs
#import  _onshape         as _on

# define tkinter object
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 350)
canvas1.pack()

title   = tk.Label(root, text='Patient Information')
label1  = tk.Label(root, text='Gender (M/F)')
label2  = tk.Label(root, text='Age (mo.)')
label3  = tk.Label(root, text='Weight (Kg.)')
label4  = tk.Label(root, text='Height (cm.)')
entry1  = tk.Entry(root)
entry2  = tk.Entry(root)
entry3  = tk.Entry(root)
entry4  = tk.Entry(root)
canvas1.create_window(200, 50, window=title)
canvas1.create_window(125, 100, window=label1)
canvas1.create_window(125, 150, window=label2)
canvas1.create_window(125, 200, window=label3)
canvas1.create_window(125, 250, window=label4)
canvas1.create_window(250, 100, window=entry1)
canvas1.create_window(250, 150, window=entry2)
canvas1.create_window(250, 200, window=entry3)
canvas1.create_window(250, 250, window=entry4)

def passData ():
    PatientData = []
    PatientData.append( entry1.get() )  #gender
    PatientData.append( entry2.get() )  #age
    PatientData.append( entry3.get() )  #weight
    PatientData.append( entry4.get() )  #height

    # do things
    print( '' )
    print( 'Calculate Blade Dimensions from Patient Database' )
    print( '================================================' )
    length, height = _is.detScopeDimensions( PatientData )
    print( '' )
    print( 'Generating 3D Blade Model' )
    print( '================================================' )
    client, element, configuration_string, response = _is.generateScope( length, height )
    
    
button1     = tk.Button(text='Enter', command=passData)
canvas1.create_window(200, 300, window=button1)

root.mainloop()
