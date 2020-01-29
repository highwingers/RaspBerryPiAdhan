dir=${PWD%/*} 
cd /etc/cron.d 
rm DailyJob
echo "1 0 * * * root /usr/bin/python3   $dir/www/commands/daily.py  >> $dir/www/commands/logs/myDailyjob.log 2>&1 # daily_run" >> DailyJob

