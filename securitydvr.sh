#!/bin/bash
PVR1_URL="http://user:user123@192.168.2.100/tmpfs/snap.jpg"
PVR1_NAME="GarageCam"
PVR2_URL="http://192.168.2.102:8080/photo.jpg"
PVR2_NAME="RackCam"
STORAGE_PATH=~/pvr

function createpaths(){
	PVRNAME=$1
	YEAR="$(date +"%Y")"
	MONTH="$(date +"%m")"
	DAY="$(date +"%d")"
	if [ ! -d "$STORAGE_PATH/$PVRNAME/$YEAR/$MONTH/$DAY" ]; then
		mkdir "$STORAGE_PATH/$PVRNAME/$YEAR/$MONTH/$DAY" -p
	fi
	echo "$STORAGE_PATH/$PVRNAME/$YEAR/$MONTH/$DAY"
}

function getimage(){
	#set -x
	URL=$1
	PVRPATH=$2
	STAMP="$(date +"%H-%M-%S")"
	wget $URL -O "$PVRPATH/$STAMP.jpg" --quiet -U "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Ubuntu/11.04 Chromium/11.0.654.0 Chrome/11.0.654.0 Safari/534.17"
	
}
function processdvrs(){
PVR1PATH=$(createpaths $PVR1_NAME)
#PVR2PATH=$(createpaths $PVR2_NAME)
getimage $PVR1_URL $PVR1PATH
#getimage $PVR2_URL $PVR2PATH
}
TIMER=0
while true; do
	TIMER=$(($TIMER + 1))
	processdvrs
	if [ "$TIMER" -gt "1000" ]; then
		rclone move ~/pvr secret:pvr &
		TIMER=0
	fi
done
