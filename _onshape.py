'''
_onshape.py

Onshape
    This cript handles the interaction between our main program and
    Onshape's Python API


Madelene Habib
Fluvio L. Lobo Fenoglietto
09/02/2020
'''

# modules
from onshape_client import OnshapeElement, Client

# variables
config_file = '.onshape_client_config.yaml'
did = '4106f8fea9cf4607edeba1db'
wid = 'c11cf0ae6ab5e6297d09562d'
eid = '3340d6f3b50b6e32e22d9a3b'


# do things
client = Client( keys_file=config_file )
element = OnshapeElement('https://cad.onshape.com/documents/{}/w/{}/e/{}'.format(did,wid,eid)) # create onshape element
response = client.part_studios_api.export_stl1(did, 'w', wid, eid, _preload_content=False)

## for configuration

# configuration=height%3D0.005%2Bmeter%3Blength%3D0.007%2Bmeter ## text for 
