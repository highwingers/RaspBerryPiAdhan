from crontab import CronTab
import datetime



dt = datetime.datetime.today()

yr = dt.year
mh = dt.month
day = dt.day #date

cron = CronTab(user='pi')
job = cron.new(command='/usr/bin/python3 /home/pi/RaspBerryPiAdhan/www/test.py "Allah is great" >> /home/pi/RaspBerryPiAdhan/www/myjob.log 2>&1 ', comment='job_fafr')
job.minute.every(1)
#job.minute.on(29)
#job.hour.on(23)
#job.month.on(mh)
#job.day.on(day)
cron.write()



##cron.remove_all(comment='job_22')
##cron.write()

