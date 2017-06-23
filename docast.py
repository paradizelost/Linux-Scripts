from __future__ import print_function
import time
import pychromecast
exroom=pychromecast.Chromecast('192.168.1.123')
lroom=pychromecast.Chromecast('192.168.1.107')
home=pychromecast.Chromecast('192.168.1.103')
emc=exroom.media_controller
lmc=lroom.media_controller
hmc=home.media_controller
home.wait()
time.sleep(5)
hmc.play_media('http://192.168.1.14/doorbell.mp3','audio/mpeg')
