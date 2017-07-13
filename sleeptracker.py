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
wsheet = gsheet.worksheet('BabySleep')
starttime= wsheet.acell('A2').value
endtime= wsheet.acell('B2').value
curtime=sys.argv[1]
print curtime
curyear = str(datetime.now().year)
curtime = datetime.strptime(curtime + ' ' + curyear,'%b %d %H:%M:%S %Y' )# 7/9/2017 17:28:46
if starttime <> '':
   if endtime <>'':
      print 'both have values, starting new row'
      wsheet.insert_row([curtime.strftime('%m/%d/%Y %H:%M:%S')],index=2)
   else:
      print 'start set, but end not, ending current set'
      starttime = datetime.strptime(starttime, '%m/%d/%Y %H:%M:%S')
      wsheet.update_acell('B2', curtime.strftime('%m/%d/%Y %H:%M:%S'))
      timebetween = curtime - starttime
      calcdiff = divmod(timebetween.total_seconds(),60)
      minutes = calcdiff[0]
      seconds = calcdiff[1]
      minutes = "%g" % round(minutes,0)
      wsheet.update_acell('C2', minutes + " Minutes" )
else:
   print 'start time not set, starting set'
   wsheet.update_acell('A2', curtime.strftime('%m/%d/%Y %H:%M:%S'))
