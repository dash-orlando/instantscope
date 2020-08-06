'''
Instant Scope


Madelene Habib
Fluvio L Lobo Fenoglietto
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Creation of gspread client
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('users.json', scope)
client = gspread.authorize(creds)


sheet = client.open('Correlations_App').sheet1


values = sheet.row_values(2)
print(values)
