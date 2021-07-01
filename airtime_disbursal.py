import os
import africastalking as at
import gspread

# Get your service account credentials file from https://console.cloud.google.com/
gc = gspread.service_account(filename='airtime-credentials.json')  # Change the name as appropriate
sh = gc.open('Contact Information (Responses)')
# print(sh.sheet1.get('B2'))


def get_spreadsheet_data(sheet_name, worksheet_index):
    sheet = gc.open(sheet_name).get_worksheet(worksheet_index)
    # by specifying the index we remove the column headers
    return sheet.get_all_values()[1:]


sheet_index = 0
g = get_spreadsheet_data('Contact Information (Responses)', sheet_index)
print(g)
for x in g:
    print(x[4])
