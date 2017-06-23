#!/usr/bin/python
import gspread
import sys
toadd=sys.argv
toadd.pop(0)
from oauth2client.service_account import ServiceAccountCredentials
scope = "https://spreadsheets.google.com/feeds"
credentials = ServiceAccountCredentials.from_json_keyfile_name('/root/bin/credentials.json', scope)
gs = gspread.authorize(credentials)
gsheet = gs.open("testsheet")
wsheet = gsheet.worksheet("Sheet1")
wsheet.insert_row(toadd,index=2)
