from datetime import datetime
from .chromecast import chromecast
from .shellcmds import shellcmd
from .Dal import Dal
import getpass
import datetime
import sys




class streamer:


    def __init__(self, media, caster, title):
        

        self.mediaUrl = media
        self.caster = caster
        self.title = title
        #self.log("Open and Close")
    def log(self, txt):
        #print(self.caster)
        self._playerLog = open('/tmp/streamer.txt', 'a')
        self._playerLog.write(txt + " " + self.caster + " "  + str(datetime.datetime.now()) + ". User:" + getpass.getuser() +  "\n\n")
        self._playerLog.close()

        Dal().LogEntry(self.caster, self.mediaUrl, self.title + " " + txt)

        
    def playMedia(self):
        pass
        try:
            self.log("Started Playing. " + self.mediaUrl)
            isBluetooth = len(self.caster.split(':'))
            if isBluetooth > 5:
                shellcmd().playBlueToothMedia(self.caster,self.mediaUrl)
            else: 
                mediaStatus = chromecast().play(self.caster, self.mediaUrl)

        except Exception as e :
            self.log("Error: " + str(e))


