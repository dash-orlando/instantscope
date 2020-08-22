'''
exportstl
===
Demos 307 redirects with the Onshape API
'''

from onshape_client import OnshapeElement, Client
import urllib.parse

# variables
config_filename = '.onshape_client_config.yaml'
did = '4106f8fea9cf4607edeba1db'
wid = 'c11cf0ae6ab5e6297d09562d'
eid = '3340d6f3b50b6e32e22d9a3b'


# do things
client = Client( config_filename ) # create client

encoded_url = urllib.parse.quote('/api/partstudios/d/4106f8fea9cf4607edeba1db/w/c11cf0ae6ab5e6297d09562d/e/3340d6f3b50b6e32e22d9a3b/stl?')
print(encoded_url)

response = client.api_client.request('GET',
                                     encoded_url,
                                     query_params=None)
