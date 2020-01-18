#!/usr/bin/python3

import sys
sys.path.append('/home/pi/RaspBerryPiAdhan/www/lib')
from datetime import datetime
from chromecast import chromecast



mediaUrl = sys.argv[1]
caster = sys.argv[2]


myFile = open('/home/pi/RaspBerryPiAdhan/www/append3.txt', 'a') 
myFile.write(mediaUrl + ' ' + caster + '/n')

mediaStatus = chromecast().play(caster, mediaUrl)