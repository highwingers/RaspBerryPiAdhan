import datetime
from PrayerPy import PrayerData
from shellcmds import shellcmd
from crontab import CronTab

class schedule:
    @staticmethod
    def adhan(lat, lng, adhanUrl, fjradhanUrl, mediaPlayer ):

        timezoneOffset =  shellcmd().getZoneOffset()
        pTimes = PrayerData(lat,lng, timezoneOffset).getTimes()

        cron = CronTab(user='pi')

        for prayer in pTimes:
            
            if prayer=="shuruq":
                continue
            if prayer=="fajr":
                media_url = fjradhanUrl               
            else:
                media_url = adhanUrl


            pTime = pTimes[prayer]
            job_id="prayer_" + prayer
            cron.remove_all(comment=job_id)        
            job = cron.new(command='/usr/bin/python3 /home/pi/RaspBerryPiAdhan/www/commands/player.py "'+ media_url +'" "'+ mediaPlayer +'"  >> /home/pi/RaspBerryPiAdhan/www/commands/logs/myjob.log 2>&1 ', comment=job_id)
            job.minute.on(pTime.minute)
            job.hour.on(pTime.hour)
            job.month.on(pTime.month)
            job.day.on(pTime.day)

        cron.write()
        
        return "Scheduled"
        
