import pychromecast

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

        print(chromecasts)
        return chromecasts

    def chromecastPlay(self, deviceName, mediaUrl):

        cast = pychromecast.get_chromecasts()[0]
        mc = cast.media_controller
        mc.play_media("http://remote.khanzone.com:8181/audio/demo.mp3", content_type = "video/mp4")
        mc.block_until_active()
        mc.play()

        return "Playing"



