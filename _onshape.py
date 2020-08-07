'''
Instant Scope :: Onshape

    This script executes onshape API calls


Madelene Habib
Fluvio L Lobo Fenoglietto
'''

# import modules
import webbrowser

# onshape variables
did = '4106f8fea9cf4607edeba1db'
wid = 'c11cf0ae6ab5e6297d09562d'
eid = '3340d6f3b50b6e32e22d9a3b'

# export STL command
cmd = 'stl?'

# execute link
webbrowser.open('https://cad.onshape.com/api/partstudios/d/{}/w/{}/e/{}/{}'.format(did,wid,eid,cmd))  # Go to example.com
