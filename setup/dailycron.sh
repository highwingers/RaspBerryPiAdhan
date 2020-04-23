dir=${PWD%/*} 
cd /etc/cron.d 
rm DailyJob
echo "1 3 * * * root /usr/bin/python3   $dir/www/daily.py  >> /tmp/DailyjobsSet.log 2>&1 # daily_run" >> DailyJob

