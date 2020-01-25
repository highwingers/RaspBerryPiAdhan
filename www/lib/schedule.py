import datetime
from lib.PrayerPy import PrayerData
from lib.shellcmds import shellcmd
from crontab import CronTab
from lib.Dal import Dal

class schedule:


    def scheduleAdhans(self, id):
        try:
            
            data = Dal().GetSettings(id)
            speaker = data[1]
            lat = data[2]
            lng = data[3]
            method = data[4]
           


            if len(speaker) > 0 :
                self.__adhan(lat, lng, method, "http://soundbible.com/mp3/cartoon-birds-2_daniel-simion.mp3", "http://soundbible.com/mp3/Kid_Laugh-Mike_Koenig-1673908713.mp3", speaker )

            return True
        except Exception as e:
            return str(e)


    def __adhan(self, lat, lng, method, adhanUrl, fjradhanUrl, mediaPlayer ):

        timezoneOffset =  shellcmd().getZoneOffset()
        pTimes = PrayerData(lat, lng, method, timezoneOffset).getTimes()
        print(pTimes)
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
        
