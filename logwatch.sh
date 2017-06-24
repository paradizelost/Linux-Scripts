#!/bin/bash
PHONE1="5555555555@vtext.com"
PHONE2="5555555555@vtext.com"
PHONE3="5555555555@vtext.com"
LOG="/var/log/logs/192.168.1.113.log"
LOG2="/var/log/logs/192.168.1.104.log"
LOG3="/var/log/logs/192.168.1.252-1.log"
EVT="$(comm  --nocheck-order -23 "$LOG" "$LOG.old" | wc -l)"
EVT2="$(comm --nocheck-order -23 "$LOG2" "$LOG2.old" | wc -l)"
EVT3="$(comm --nocheck-order -23 "$LOG3" "$LOG3.old" | wc -l)"
function procaplog(){
	while IFS=, read -r date mac; do
		echo "starting mac check"
		echo "starting mac check" >> /var/log/logwatch.log
		HOSTNAME=$(checkmac $mac)
		if [ "$HOSTNAME" ]; then 
			echo "__ $HOSTNAME __"
			echo "__ $HOSTNAME __" >> /var/log/logwatch.log
			case $HOSTNAME in
			AMAZON_IOT_BUTTON)
				/root/bin/sheet.py "$date" "Diaper Change" 
				alert_dan "$date The button was pushed" 
				python /root/bin/docast.py
				;;
			DAN_PIXEL)
				echo "Alerting Alli"
				echo "Alerting Alli" >> /var/log/logwatch.log
				alert_alli "Dan is home at $date" 
				/root/bin/sheet.py "$date" $HOSTNAME
				;;
			*)
				echo "No Match with -$HOSTNAME- alerting"
				echo "No Match with -$HOSTNAME- alerting">> /var/log/logwatch.log
				/root/bin/sheet.py "$date" $HOSTNAME
				;;
			esac
		else
			echo "$mac"
			alert_dan "$NOW - Unknown host $mac connected at $date"
			/root/bin/sheet.py  "$date" $mac
		fi
	done
};
function procswitchlog(){
	echo "$1" >> /var/log/logwatch.log
	echo "$1"
	while IFS=, read -r date device port state; do
		if [ "$state" == "Up:" ]; then 
			alert_dan "Port $port on switch $device came up at $date"
		else 
			alert_dan "Port $port on switch $device went down at $date"
		fi
	done
}
function checkmac(){
	LINE=$(grep "$1" /root/bin/test.txt )
	if [ "$LINE" ]; then
		read -r mac hostname <<< $LINE
		echo "$hostname"
		echo "$hostname"  >> /var/log/logwatch.log
	fi
};
function alert_alli(){
	echo "$1"
	echo "$1" >> /var/log/logwatch.log
	nail -s "$1" -S from="Alerts@hamik.net" "$PHONE2" <<<"."
};
function alert_dan(){
	echo "$1"
	echo "$1" >> /var/log/logwatch.log
	nail -s "$1" -S from="Alerts@hamik.net" "$PHONE1" <<<"."
	nail -s "$1" -S from="Alerts@hamik.net" "$PHONE3" <<<"."
};

if [ "$EVT" != "0" ]; then
	cp "$LOG" "$LOG.old" 
	tail -n "$EVT" "$LOG" |  awk '/WPA: pairwise key handshake completed/ {print $1 " " $2 " " $3 ", " $9 }'|procaplog
fi
if [ "$EVT2" != "0" ]; then
	cp "$LOG2" "$LOG2.old" 
	tail -n "$EVT2" "$LOG2" |  awk '/WPA: pairwise key handshake completed/ {print $1 " " $2 " " $3 ", " $9 }'|procaplog
fi
if [ "$EVT3" != "0" ]; then
	cp "$LOG3" "$LOG3.old" 
	#tail -n "$EVT3" "$LOG3" |  awk '/Link Up:/ {print $1 " " $2 " " $3 "," $4 "," $11 "," $10 }'|procswitchlog
	#tail -n "$EVT3" "$LOG3" |  awk '/Link Down:/ {print $1 " " $2 " " $3 "," $4 "," $11 "," $10}'|procswitchlog
fi
