'''
exportstl
===
Demos 307 redirects with the Onshape API
'''

# modules
import requests
import json
from onshape_client import OnshapeElement, Client

# variables
config_filename = '.onshape_client_config.yaml'
did = '4106f8fea9cf4607edeba1db'
wid = 'c11cf0ae6ab5e6297d09562d'
eid = '3340d6f3b50b6e32e22d9a3b'


# do things
client = Client( config_filename )

response = requests.get(    'https://cad.onshape.com/api/partstudios/d/{}/w/{}/e/{}/stl'.format(did,wid,eid),
                            params=client.configuration.api_key )

print(response.url)
