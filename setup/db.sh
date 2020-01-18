#!/bin/bash
file="/home/pi/RaspBerryPiAdhan/www/data/adhan.db"
if [ -f "$file" ]
then
	echo "$file found."
else
	python3 /home/pi/RaspBerryPiAdhan/www/data/db.py
fi

