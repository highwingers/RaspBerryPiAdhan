#!/usr/bin/python3

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from datetime import datetime
from lib.chromecast import chromecast
from lib.shellcmds import shellcmd



mediaUrl = sys.argv[1]
caster = sys.argv[2]


isBluetooth = len(caster.split(':'))
if isBluetooth > 5:
    shellcmd().playBlueToothMedia(caster,mediaUrl)
else: 
    mediaStatus = chromecast().play(caster, mediaUrl)

#myFile = open('.logs/errors.txt', 'a') 
#myFile.write(mediaUrl + ' ' + caster + '/n')

