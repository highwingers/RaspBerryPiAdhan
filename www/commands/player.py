#!/usr/bin/python3

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from datetime import datetime
from lib.chromecast import chromecast



mediaUrl = sys.argv[1]
caster = sys.argv[2]


#myFile = open('/home/pi/RaspBerryPiAdhan/www/append3.txt', 'a') 
#myFile.write(mediaUrl + ' ' + caster + '/n')

mediaStatus = chromecast().play(caster, mediaUrl)