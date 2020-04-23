#!/usr/bin/python3

import pathlib
from lib.schedule import schedule
from lib.Dal import Dal

_currentDirectoy = pathlib.Path(__file__).parent.absolute()
playerPath =  str(_currentDirectoy) + '/player.py'




scheduleAdhan = schedule().scheduleAdhans(1,playerPath)
Dal().LogEntry("", "", "Prayers Schedule For Today")
Dal().DeleteLogs()
