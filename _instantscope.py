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

    # Extract Data and Labels
    # ------------------------------------------------------ #
    type_labels     = _gs.getColumnValues(gs_client, 'Correlations_App', 1)
    corr_l_col      = _gs.getColumnValues(gs_client, 'Correlations_App', 2)
    corr_h_col      = _gs.getColumnValues(gs_client, 'Correlations_App', 5)

    # Determine Correlation Indeces
    # ------------------------------------------------------ #
    corr_l_values = []
    corr_h_values = []
    for i in range( 1, len(corr_l_col) ):
        # note that this loop purposely skips the first row
        # to avoid errors on the float() conversion
        corr_l_values.append( float( corr_l_col[i] ) )
        corr_h_values.append( float( corr_h_col[i] ) )
    max_corr_l = max(corr_l_values)
    max_corr_h = max(corr_h_values)
    max_corr_l_index = corr_l_values.index( max_corr_l ) + 1 # here we add the +1 to account for skipping over the first row
    max_corr_h_index = corr_h_values.index( max_corr_h ) + 1 # ...

    print( 'Best correlation available are;' )
    print( 'Blade Length and Patient {}, with R2={}'.format( type_labels[max_corr_l_index], corr_l_col[max_corr_l_index] ) )
    print( 'Blade Height and Patient {}, with R2={}'.format( type_labels[max_corr_h_index], corr_h_col[max_corr_h_index] ) )


    # Get Row Values that Match Best Correlations
    # ------------------------------------------------------ #
    corr_l_row = _gs.getRowValues(gs_client, 'Correlations_App', max_corr_l_index + 1) # we use a +1 to correct for the labels on the first column
    corr_h_row = _gs.getRowValues(gs_client, 'Correlations_App', max_corr_h_index + 1) # ...

    # Extract Coefficients
    # ------------------------------------------------------ #
    m_l = float( corr_l_row[2] )
    b_l = float( corr_l_row[3] )
    m_h = float( corr_h_row[5] )
    b_h = float( corr_h_row[6] )

    print( 'The correlation coefficients are as follows;' )
    print( 'Blade Length and Patient {}, {}X + {}'.format( type_labels[max_corr_l_index], m_l, b_l ) )
    print( 'Blade Height and Patient {}, {}X + {}'.format( type_labels[max_corr_h_index], m_h, b_h ) )
    
    # Calculate the Length and Height of the Blade
    # ------------------------------------------------------ #
    length = m_l*float(PatientData[max_corr_l_index]) + b_l
    height = m_h*float(PatientData[max_corr_h_index]) + b_h

    print( 'Based on these correlation equations, the blade dimensions are as follows;' )
    print( 'Blade Length = {} cm'.format( length ) )
    print( 'Blade Height = {} cm'.format( height ) )

    length_in_meters = length / 100
    height_in_meters = height / 100
    
    return length_in_meters, height_in_meters
    
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
