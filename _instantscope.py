'''
Instant Scope

    This script calculates the proper
    laryngoscope model dimensions

Madelene Habib
Fluvio L Lobo Fenoglietto
'''

# import modules
#import _gui
import _gspread as _gs



# functions

def getPatientData( PatientData ):
    print( PatientData )


def detScopeDimensions( PatientData ):

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

    # calculate length and height
    length = m_l*float(PatientData[max_corr_l_index + 1]) + b_l
    height = m_h*float(PatientData[max_corr_h_index + 1]) + b_h

    print(length, height)

    return length, height
    
