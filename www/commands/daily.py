#!/usr/bin/python3

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from lib.schedule import schedule
from lib.Dal import Dal
#print(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))




currentDirectory = os.path.dirname(os.path.realpath(__file__))
playerPath = currentDirectory + '/player.py'

#f = open("demofile2.txt", "a")
#f.write(playerPath)
#f.close()


scheduleAdhan = schedule().scheduleAdhans(1,playerPath)
Dal().LogEntry("", "", "Prayers Schedule For Today")
Dal().DeleteLogs()
