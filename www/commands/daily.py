#!/usr/bin/python3

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from lib.schedule import schedule

#print(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

scheduleAdhan = schedule().scheduleAdhans(1)
