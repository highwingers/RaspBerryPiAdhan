import sys
sys.path.append('../')
from lib.shellcmds import shellcmd
from lib.chromecast import chromecast

ip = shellcmd().command("hostname -I")
url = 'http://'+ip+'/static/media/demo.mp3'
chromecast().chromecastPlay('Office Ustairs speaker', url)



