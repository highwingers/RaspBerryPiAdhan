import subprocess
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

    def getZoneOffset(self):
        try:
            cmd = "date +'%:z %Z'"
            result = self.command(cmd).split(":")[0]
            return int(result)
        except :
            return 0
