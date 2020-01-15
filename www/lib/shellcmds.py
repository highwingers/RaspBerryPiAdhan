import subprocess
class shellcmd:
    def __init__(self):
        pass
    def command(self, cmd):
        result = subprocess.run([cmd], stdout=subprocess.PIPE, shell=True)
        r =  result.stdout
        r = r.decode("utf-8").replace('\n',' ').strip()
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
