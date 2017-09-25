#!/usr/bin/python
from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
	htmlstring = "<html>\n<body>"
	htmlstring += "<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\"><br/><br/>"
	htmlstring += "<a href='/sleep' class='button'>Sleep</a><br/><br/>\n "
	htmlstring += "<a href='/wetdiaper' class='button'>Wet Diaper</a><br/><br/>\n "
	htmlstring += "<a href='/dirtydiaper' class='button'>Dirty Diaper</a><br/><br/>\n "
	htmlstring += "<a href='/feeding' class='button'>Feeding</a>\n "
	htmlstring += "</div>\n</body>\n</html>"
	return htmlstring

@app.route("/sleep")
def sleep():
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
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
	gs = gspread.authorize(credentials)
	gsheet = gs.open("testsheet")
	wsheet = gsheet.worksheet('BabySleep')
	starttime= wsheet.acell('A2').value
	endtime= wsheet.acell('B2').value
	curtime=datetime.now()
	print curtime
	if starttime <> '':
	   if endtime <>'':
	      wsheet.insert_row([curtime.strftime('%m/%d/%Y %H:%M:%S')],index=2)
	      return 'Sleep Start Time Logged\n<meta http-equiv="refresh" content="1,url=/" />'
	   else:
	      starttime = datetime.strptime(starttime, '%m/%d/%Y %H:%M:%S')
	      wsheet.update_acell('B2', curtime.strftime('%m/%d/%Y %H:%M:%S'))
	      timebetween = curtime - starttime
	      calcdiff = divmod(timebetween.total_seconds(),60)
	      minutes = calcdiff[0]
	      seconds = calcdiff[1]
	      minutes = "%g" % round(minutes,0)
	      wsheet.update_acell('C2', minutes)
	      return 'Sleep End Time Logged\n<meta http-equiv="refresh" content="1,url=/" />'
	else:
	   wsheet.update_acell('A2', curtime.strftime('%m/%d/%Y %H:%M:%S'))
	   return 'Sleep Start Time Logged\n<meta http-equiv="refresh" content="1,url=/" />'
@app.route("/wetdiaper")
def wet():
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
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
	gs = gspread.authorize(credentials)
	gsheet = gs.open("testsheet")
	wsheet = gsheet.worksheet("DiaperChange")
	curtime=datetime.now()
	wsheet.insert_row([curtime.strftime('%m/%d/%Y %H:%M:%S'),'WET'],index=2)
	return 'Wet Diaper Logged\n<meta http-equiv="refresh" content="1,url=/" />'
@app.route("/dirtydiaper")
def dirty():
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
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
	gs = gspread.authorize(credentials)
	gsheet = gs.open("testsheet")
	wsheet = gsheet.worksheet("DiaperChange")
	curtime=datetime.now()
	wsheet.insert_row([curtime.strftime('%m/%d/%Y %H:%M:%S'),'DIRTY'],index=2)
	return 'Dirty Diaper Logged\n<meta http-equiv="refresh" content="1,url=/" />'
@app.route("/feeding")
def feeding():
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
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
	gs = gspread.authorize(credentials)
	gsheet = gs.open("testsheet")
	wsheet = gsheet.worksheet("Feeding")
	curtime=datetime.now()
	wsheet.insert_row([curtime.strftime('%m/%d/%Y %H:%M:%S')],index=2)
	return 'Feeding Logged\n<meta http-equiv="refresh" content="1,url=/" />'

