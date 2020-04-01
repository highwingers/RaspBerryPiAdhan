import subprocess
from pathlib import Path
class shellcmd:
    def __init__(self):
        pass
    def command(self, cmd, removeNewLine=True):
        result = subprocess.run([cmd], stdout=subprocess.PIPE, shell=True)
        r =  result.stdout
        
        if removeNewLine:
            r = r.decode("utf-8").replace('\n',' ').strip()
        else: 
            r = r.decode("utf-8").strip()
        
        return r

    def setTimeZone(self,timezone):
        cmd = "timedatectl set-timezone " + timezone
        result = self.command(cmd)


    def setBluetoothSpeaker(self,mac):
        _cmd  = "sudo -u pi sh " +  str(Path(__file__).parent.parent.parent) + "/setup/set-speaker.sh " + mac
        print(_cmd)
        result = self.command(_cmd)
        print(result)

    def playBlueToothMedia(self, mac, media):
        _mediapath=media
        if not media.startswith("http"):
            _mediapath = str(Path(__file__).parent.parent) + media
        #self.command("whoami > ./whoami.txt",False)
        _connect = shellcmd().command("{   printf 'trust "+ mac +"\n\n';     sleep 5;     printf 'pair "+ mac +"\n\n';     sleep 5;     printf 'connect "+ mac +"\n\n';     sleep 5; } |  sudo bluetoothctl", False)
        self.command("pkill mplayer")
        _play = self.command("sudo -u pi mplayer '"+ _mediapath +"' -ao alsa:device=bluealsa")
        _disconnect = self.command("{   printf 'disconnect "+ mac +"\n\n';     sleep 5;      } |  sudo bluetoothctl", False)
        return _play

    def getZoneOffset(self):
        try:
            cmd = "date +'%:z %Z'"
            result = self.command(cmd).split(":")[0]
            return int(result)
        except :
            return 0
