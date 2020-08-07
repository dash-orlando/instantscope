'''
Instant Scope


Madelene Habib
Fluvio L Lobo Fenoglietto
'''

# import modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# functions
def setupClient():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('users.json', scope)
    client = gspread.authorize(creds)
    return client

def getColumnValues(client, filename, column):
    sheet = client.open( filename ).sheet1
    values = sheet.col_values( column )
    return values

def getRowValues(client, filename, row):
    sheet = client.open( filename ).sheet1
    values = sheet.row_values( row )
    return values
