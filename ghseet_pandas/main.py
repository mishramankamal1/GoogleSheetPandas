import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

SHEET_ID = '1y5ibZpTsmNmZginPqp_1JIoHTNrVmJWUBVcbrpHgeUs'
SHEET_NAME = "test"


def get_dataframe():
    data = [['Mankamal', 10], ['Punam', 15], ['Kamal', 14], ['Manu', 15]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    return df


def _get_worksheet(key: str, worksheet_name: str, creds="gCredentials.json") -> gspread.Worksheet:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)
    gc = gspread.authorize(credentials)
    wb = gc.open_by_key(key)
    sheet = wb.worksheet(worksheet_name)
    return sheet


def write(sheet: gspread.Worksheet, df: pd.DataFrame) -> None:
    cells = sheet.get_all_values()
    set_with_dataframe(sheet, df, include_index=False,
                       include_column_header=False, row=len(cells) + 1, resize=False)


sh = _get_worksheet(SHEET_ID, SHEET_NAME)

write(sh, get_dataframe())
