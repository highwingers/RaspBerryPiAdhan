import datetime
from .PrayerPy import PrayerData
from .shellcmds import shellcmd
from crontab import CronTab
from .Dal import Dal

class schedule:


    def scheduleAdhans(self, id):
        try:
            data = Dal().GetSettings(id)
            speaker = data[1]
            lat = data[2]
            lng = data[3]
            method = data[4]
           


            if len(speaker) > 0 :
                self.__adhan(lat, lng, method,  speaker )
        
            return True
        except Exception as e:
            return str(e)


    def __adhan(self, lat, lng, method, mediaPlayer ):

        timezoneOffset =  shellcmd().getZoneOffset()
        pTimes = PrayerData(lat, lng, method, timezoneOffset).getTimes()
        #print(pTimes)
        cron = CronTab(user='pi')
        _data = Dal().GetAdhanSettings(1)

        _prayDb = {}
        for x in _data:
            _prayDb[x[3]] = {"prayer": x[3], "status": x[5], "media": x[4]}


        print(_prayDb)

        for prayer in pTimes:
            
            pTime = pTimes[prayer]
            job_id="prayer_" + prayer
            cron.remove_all(comment=job_id)      
            
            if prayer=="shuruq":
                continue

            if prayer=="fajr" :
                media_url = _prayDb["FAJR"]["media"]
                if _prayDb["FAJR"]["status"]==0:
                    continue   
            if prayer=="zuhr" :
                media_url = _prayDb["DUHUR"]["media"]
                if _prayDb["DUHUR"]["status"]==0:
                    continue
            if prayer=="asr" :
                media_url = _prayDb["ASR"]["media"]
                if _prayDb["ASR"]["status"]==0:
                    continue
            if prayer=="maghrib" :
                media_url = _prayDb["MAGRIB"]["media"]
                if _prayDb["MAGRIB"]["status"]==0:
                    continue
            if prayer=="isha" :
                media_url = _prayDb["ISHA"]["media"]
                if _prayDb["ISHA"]["status"]==0:
                    continue

            job = cron.new(command='/usr/bin/python3 /home/pi/RaspBerryPiAdhan/www/commands/player.py "'+ media_url +'" "'+ mediaPlayer +'"  >> /home/pi/RaspBerryPiAdhan/www/commands/logs/myjob.log 2>&1 ', comment=job_id)
            job.minute.on(pTime.minute)
            job.hour.on(pTime.hour)
            job.month.on(pTime.month)
            job.day.on(pTime.day)

        cron.write()
        
        return "Scheduled"
        
