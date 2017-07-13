#!/usr/bin/python
import gspread
import sys
import time
import datetime
from datetime import datetime
#toadd=sys.argv
#toadd.pop(0)
#mydate=sys.argv[0]
#buttonname=sys.argv[1]
from oauth2client.service_account import ServiceAccountCredentials
scope = "https://spreadsheets.google.com/feeds"
credentials = ServiceAccountCredentials.from_json_keyfile_name('/root/bin/credentials.json', scope)
gs = gspread.authorize(credentials)
gsheet = gs.open("testsheet")
wsheet = gsheet.worksheet("Feeding")
curtime=sys.argv[1]
curyear = str(datetime.now().year)
curtime = datetime.strptime(curtime + ' ' + curyear,'%b %d %H:%M:%S %Y' )# 7/9/2017 17:28:46
wsheet.insert_row([curtime.strftime('%m/%d/%Y %H:%M:%S')],index=2)
