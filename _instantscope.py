'''
Instant Scope

    This script calculates the proper
    laryngoscope model dimensions

Madelene Habib
Fluvio L Lobo Fenoglietto
'''

# import modules
import _gspread as _gs
import _onshape as _on

# variables
config_file = '.onshape_client_config.yaml'                                                     # configuration file
document_url = 'https://cad.onshape.com/documents/4106f8fea9cf4607edeba1db/w/c11cf0ae6ab5e6297d09562d/e/3340d6f3b50b6e32e22d9a3b'

# Functions
# ----------------------------------------------------------- #

def getPatientData( PatientData ):
    print( PatientData )

# ----------------------------------------------------------- #

def detScopeDimensions( PatientData ):

    '''
        detPatientData();
        - Determine the patient-specific data needed to build the laryngoscope
    '''
    #
    ## WARNING: The current version of this program
    ## requires that all of the patient information
    ## is provided up-front
    #

    gs_client = _gs.setupClient()

    # pick the best correlation
    corr_l_col = _gs.getColumnValues(gs_client, 'Correlations_App', 2)
    corr_h_col = _gs.getColumnValues(gs_client, 'Correlations_App', 5)

    corr_l_values = []
    corr_h_values = []
    for i in range(1, len(corr_l_col)):
        corr_l_values.append( float( corr_l_col[i] ) )
        corr_h_values.append( float( corr_h_col[i] ) )
    max_corr_l = max(corr_l_values)
    max_corr_h = max(corr_h_values)
    max_corr_l_index = corr_l_values.index( max_corr_l )
    max_corr_h_index = corr_h_values.index( max_corr_h )
    print( corr_l_values, max_corr_l, max_corr_l_index)

    # get values from rows 
    corr_l_row = _gs.getRowValues(gs_client, 'Correlations_App', max_corr_l_index + 2) # the +2 is a correction of indeces
    corr_h_row = _gs.getRowValues(gs_client, 'Correlations_App', max_corr_h_index + 2)
    #print(corr_l_row)
    #print(corr_h_row)
    
    m_l = float( corr_l_row[2] )
    b_l = float( corr_l_row[3] )

    m_h = float( corr_h_row[5] )
    b_h = float( corr_h_row[6] )

    print( m_l, b_l, m_h, b_h )

    # here we need to handle the lack of values in the input...  i.e. missing the weight of the patient...
    
    # calculate length and height
    length = ( m_l*float(PatientData[max_corr_l_index + 1]) + b_l )/1000
    height = ( m_h*float(PatientData[max_corr_h_index + 1]) + b_h )/1000

    print( length, height )

    return length, height
    
# ----------------------------------------------------------- #

def generateScope( length, height ):

    '''
        genScope()
        - Uses the Onshape API functions to;
        -- Modify the configuration parameters of a base PartStudio
        -- Export modified PartStudio as an .STL file
    '''

    client                  = _on.openClient( config_file )
    element                 = _on.createOnshapeElement( document_url )
    configuration_string    = _on.generateConfigurationString( height, length )
    response                = _on.exportPart( client, element, configuration_string )

    return client, element, configuration_string, response
