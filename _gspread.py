'''
Instant Scope


Madelene Habib
Fluvio L Lobo Fenoglietto
'''

# Import Modules and Libraries
# ----------------------------------------------------------- #
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Functions
# ----------------------------------------------------------- #

def setupClient():
    '''
        setupClient()
        - Creates/opens google sheets client
    '''
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('users.json', scope)
    client = gspread.authorize(creds)
    return client

# ----------------------------------------------------------- #

def getColumnValues(client, filename, column):
    '''
        getColumnValues()
        - Retrieves all values in a given row
    '''
    sheet = client.open( filename ).sheet1
    values = sheet.col_values( column )
    return values

# ----------------------------------------------------------- #

def getRowValues(client, filename, row):
    '''
        getRowValues()
        - Retrieves all values in a given row
    '''
    sheet = client.open( filename ).sheet1
    values = sheet.row_values( row )
    return values
