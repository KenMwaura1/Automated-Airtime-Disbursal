import os
import africastalking as at 
from dotenv import load_dotenv
import gspread

# Get your service account credentials file from https://console.cloud.google.com/
gc = gspread.service_account(filename='airtime-credentials.json')  # Change the name as appropriate
sh = gc.open('Contact Information (Responses)')
# print(sh.sheet1.get('B2'))

# Load our sensitive information using environment variables
load_dotenv()
# get the environment values from the .env file
at_username = os.getenv('at_username')
at_api_key = os.getenv('at_api_key')

# initialize africas talking using username and api key
at.initialize(at_username, at_api_key)
airtime = at.Airtime
account = at.Application


def get_spreadsheet_data(sheet_name, worksheet_index):
    sheet = gc.open(sheet_name).get_worksheet(worksheet_index)
    # by specifying the index we remove the column headers
    return sheet.get_all_values()[1:]


sheet_index = 0
airtime_sheet_name = 'Contact Information (Responses)'
sheet_data = get_spreadsheet_data(airtime_sheet_name, sheet_index)
print(sheet_data)


def airtime_disbursal(number, airtime_amount: str, airtime_currency_code: str):
    print(account.fetch_application_data())

    try:
        response = airtime.send(phone_number=number, amount=amount, currency_code=currency_code)
        print(response)
    except Exception as e:
        print(f"Encountered an error while sending airtime. More error details below\n {e}")


# Set The 3-Letter ISO currency code and the amount
amount = "5"
currency_code = "KES"

# Unpack the list of values
for item in sheet_data:
    print(item[4])
    mobile_number = item[4]
    # for each number in the sheet send airtime top-up as specified.
    # airtime_disbursal(mobile_number, amount, currency_code)

print(account.fetch_application_data())

