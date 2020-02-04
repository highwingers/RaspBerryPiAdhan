import datetime
from datetime import datetime
from croniter import croniter
from .PrayerPy import PrayerData
from .shellcmds import shellcmd
from crontab import CronTab
from .Dal import Dal

class schedule:


    def scheduleAdhans(self, id, playerPath):
        try:
            data = Dal().GetSettings(id)
            speaker = data[1]
            lat = data[2]
            lng = data[3]
            method = data[4]
            asr = data[5]
           


            if len(speaker) > 0 :
                self.__adhan(lat, lng, method, asr,  speaker, playerPath )
        
            return True
        except Exception as e:
            return str(e)

        # ONCE      8
        # DAILY     7
        #    0 - Sun      Sunday
        #    1 - Mon      Monday
        #    2 - Tue      Tuesday
        #    3 - Wed      Wednesday
        #    4 - Thu      Thursday
        #    5 - Fri      Friday
        #    6 - Sat      Saturday
        #    7 - Sun      Sunday
    def AddSchedule(self, id, _date, title,playerPath, media_url, frequency, speaker):

        try:
         
            cron = CronTab(user='pi')
            job = cron.new(command='/usr/bin/python3 '+ playerPath +' "'+ media_url +'" "'+ speaker +'" >> .error.log  2>&1', comment=title)

            if frequency=='8':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.month.on(_date.month)
                job.day.on(_date.day)
            elif frequency=='0':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('SUN')
            elif frequency=='1':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('MON')
            elif frequency=='2':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('TUE')
            elif frequency=='3':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('WED')
            elif frequency=='4':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('THU')
            elif frequency=='5':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('FRI')
            elif frequency=='6':
                job.minute.on(_date.minute)
                job.hour.on(_date.hour)
                job.dow.on('SAT')
            else: 
                job.minute.on(_date.minute)
                job.hour.on(_date.hour) 

            cron.write()

            #DB Write
            #print("============================" + speaker)
            Dal().AddSchedule(title,str(_date),frequency,speaker)
                
        except Exception as e :
            print(str(e))





    def __adhan(self, lat, lng, method, asr, mediaPlayer, playerPath ):

        timezoneOffset =  shellcmd().getZoneOffset()
        pTimes = PrayerData(lat, lng, method, asr, timezoneOffset).getTimes()
        #print(pTimes)
        cron = CronTab(user='pi')
        _data = Dal().GetAdhanSettings(1)

        _prayDb = {}
        for x in _data:
            _prayDb[x[3]] = {"prayer": x[3], "status": x[5], "media": x[4]}


        #print(_prayDb)

        for prayer in pTimes:
            
            pTime = pTimes[prayer]
            job_id="prayer_" + prayer
            cron.remove_all(comment=job_id)      
            Dal().DeleteSchedule(job_id)

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

            job = cron.new(command='/usr/bin/python3 '+ playerPath +' "'+ media_url +'" "'+ mediaPlayer +'"', comment=job_id)
            job.minute.on(pTime.minute)
            job.hour.on(pTime.hour)
            job.month.on(pTime.month)
            job.day.on(pTime.day)

            #DB Write
            #print("============================" + str(pTime))
            
            Dal().AddSchedule(job_id,str(pTime),9,mediaPlayer)


        cron.write()



        
        return "Scheduled"


    def queryJobs(self) :
        cmd = 'crontab -l -u pi | grep -E "^@|^\*|^[0-9]" | sort -n -k2 -k1 | awk -F"#" \'{split($1,a," "); print a[1] " " a[2] " " a[3] " " a[4] " " a[5] "|"   $2}\' '
        c = shellcmd().command(cmd, False)
        lines = c.splitlines()
        base = datetime.now()
        dates=[]
        for line in lines:
            fullline = line.split("|")
            _month = fullline[0].split(" ")[3]
            _date = fullline[0].split(" ")[2]

            iter = croniter(fullline[0], base, False)  # every 5 minutes
            _nextdate = iter.get_next(datetime)             

            obj = {'nextFireDate': _nextdate, 'title': fullline[1]}
            if _nextdate.year==datetime.today().year: 
                dates.append(obj)

        a = sorted(dates, key=lambda x: x['nextFireDate'])   
        return a


        
