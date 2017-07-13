#!/usr/bin/python
from __future__ import print_function
import time
import pychromecast
home=pychromecast.Chromecast('192.168.1.103')
home.media_controller.play_media("http://192.168.1.14/doorbell.mp3",'audio/mpeg')
home.wait()
