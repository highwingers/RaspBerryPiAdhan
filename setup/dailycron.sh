cd /etc/cron.d
echo "1 * * * * root /usr/bin/python3 /home/pi/RaspBerryPiAdhan/www/commands/daily.py  >> /home/pi/RaspBerryPiAdhan/www/commands/logs/myDailyjob.log 2>&1 # daily_run" >> DailyJob



