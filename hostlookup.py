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
wsheet = gsheet.worksheet("Hosts")
#starttime= wsheet.acell('A2').value
#endtime= wsheet.acell('B2').value
macaddr=sys.argv[1]
curtime=sys.argv[2]
curyear = str(datetime.now().year)
curtime = datetime.strptime(curtime + ' ' + curyear,'%b %d %H:%M:%S %Y' )# 7/9/2017 17:28:46
cell = wsheet.find(macaddr)
if cell is not None:
   hostname = wsheet.cell(cell.row,cell.col+1)
   lastseencolumn = cell.col + 2
   wsheet.update_cell(cell.row,lastseencolumn,curtime)
   print hostname.value
else:
   wsheet.insert_row([macaddr,'UNKOWN_HOST',curtime],index=2)
   print "UNKNOWN_HOST"
#if starttime <> '':
# wsheet.appendrow();
#else:
