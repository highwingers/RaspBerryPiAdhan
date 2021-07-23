import pychromecast
import time
from pychromecast.controllers.youtube import YouTubeController
from urllib.parse import urlparse,parse_qs
from .shellcmds import shellcmd
from .utility import utility

class chromecast:
        

    def __init__(self):
        pass

    def chromecastQuery(self):
        _chromecast_devices = pychromecast.get_chromecasts()
        chromecasts = []
        for cast in _chromecast_devices:
            device = {
                'name': cast.name,
                'cast_type': cast.cast_type,
                'model_name': cast.model_name,
                'uuid': str(cast.uuid),
                'manufacturer': cast.device.manufacturer
            }
            chromecasts.append(device)

        return chromecasts


    def play(self, deviceName, media):

        if "youtube.com" in media:
            return self.chromecastPlayYoutube(deviceName, media)
        elif  not media.startswith("http"): 
            ip = shellcmd().command("ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p'")
            _port =  ':' + utility.ConfigSectionMap("SetUp")["port"]
            media = 'http://'+ ip + _port + media

        return self.chromecastPlay(deviceName, media)



    def chromecastPlay(self, deviceName, mediaUrl):

        url = mediaUrl
        chromecasts = pychromecast.get_chromecasts()
        cast = next(cc for cc in chromecasts if cc.device.friendly_name == deviceName)
        cast.wait()    
        #cast.quit_app()
        mc = cast.media_controller
        mc.play_media(url, 'audio/mp4')
        mc.block_until_active()
        #print(mc.status)
        mc.pause()
        time.sleep(2)
        mc.play()

        return "Playing Media"

    def chromecastPlayYoutube(self, deviceName, mediaUrl): 
        
        CAST_NAME = deviceName

        # Change to the video id of the YouTube video
        # video id is the last part of the url http://youtube.com/watch?v=video_id
        url_data = urlparse(mediaUrl)
        query = parse_qs(url_data.query)
        VIDEO_ID = query["v"][0]
        print(VIDEO_ID)

        chromecasts = pychromecast.get_chromecasts()
        cast = next(cc for cc in chromecasts if cc.device.friendly_name == deviceName)
        cast.wait()
        yt = YouTubeController()
        cast.register_handler(yt)
        yt.play_video(VIDEO_ID)
        return "Playing Youtube"
