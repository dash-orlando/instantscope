'''
_onshape.py

Onshape
    This cript handles the interaction between our main program and
    Onshape's Python API


Madelene Habib
Fluvio L. Lobo Fenoglietto
09/02/2020
'''

# Modules and Libraries
# ----------------------------------------------------------- #
from onshape_client import OnshapeElement, Client

# Default Variables
# ----------------------------------------------------------- #
config_file = '.onshape_client_config.yaml'                                                     # configuration file
document_url = 'https://cad.onshape.com/documents/4106f8fea9cf4607edeba1db/w/c11cf0ae6ab5e6297d09562d/e/3340d6f3b50b6e32e22d9a3b'

# Functions
# ----------------------------------------------------------- #

def openClient( config_file ):
    '''
        openClient();
        - Create/Open Onshape API Client
        - Requires the file path to the config YAML file with API KEYS
    '''
    client = Client( keys_file=config_file )
    return client

# ----------------------------------------------------------- #

def createOnshapeElement( document_url ):
    '''
        createOnshapeElement();
        - Creates Onshape Element from document URL
    '''
    element = OnshapeElement( document_url )
    print( 'Created Onshape Element from {}'.format( element.name ) )
    return element

# ----------------------------------------------------------- #

def generateConfigurationString( height, length ):
    '''
        generateConfigurationString();
        - Generates proper string to modify configuration parameters

        * In the future, this function should be deprecated for 
    '''
    configuration_string = 'configuration=height%3D{}%2Bmeter%3Blength%3D{}%2Bmeter'.format( height, length )
    print( 'Generated configuration string {}'.format( configuration_string ) )
    return configuration_string

# ----------------------------------------------------------- #

def exportPart( client, element, configuration_string ):
    '''
        exportPart();
        - Exports workspace Part as an STL using the variables Onshape Element and 'configuration_string'
    '''
    did = element.did
    wvm = element.wvm
    wid = element.wvmid
    eid = element.eid
    response = client.part_studios_api.export_stl1(did, wvm, wid, eid, _preload_content=False, configuration=configuration_string )

    if response.status == 200:
        print( 'Request Successful, Response = {}'.format( response.status ) )

        print( 'Writing part file as {}.STL (binary)'.format( element.name ) )
        with open( '{}.stl'.format( element.name ), 'wb' ) as file:
            file.write( response.data )
        file.close()
        
    else:
        print( 'ERROR: Response = {}'.format( response.status ) )

    return response


