from __future__ import print_function
import time
import onshape_client.oas
from pprint import pprint

#from onshape_client.client import Client

config_filename = '.onshape_client_config.yaml'
#client = Client( keys_file=config_filename )


configuration = onshape_client.oas.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
#configuration.api_key = client.configuration.api_key
#configuration.api_key = {'SECRET_KEY': 'CJ1MZi2mdI6hyYyr29JXE5FdkMbKfR6JQryR66DL4r6Z7HiV',
#                         'ACCESS_KEY': 'eSTHTCURZ3DEWUhuubalV3IS'}
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://cad.onshape.com
configuration.host = "https://cad.onshape.com"


# Enter a context with an instance of the API client
api_client = onshape_client.oas.ApiClient(configuration)

# Create an instance of the API class
api_instance = onshape_client.oas.PartStudiosApi(api_client)
did = '4106f8fea9cf4607edeba1db' # str | 
wid = 'c11cf0ae6ab5e6297d09562d' # str | 
eid = '3340d6f3b50b6e32e22d9a3b' # str |

try:
    api_response = api_instance.export_stl1(did, 'w', wid, eid)
    print(api_response)
except onshape_client.oas.ApiException as e:
    print("Exception when calling AssembliesApi->get_feature_specs: %s\n" % e)

