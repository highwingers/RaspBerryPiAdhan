import pychromecast


chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Kitchen display")
cast.wait()
print(cast.device)
print(cast.status)
mc = cast.media_controller
mc.play_media('http://remote.khanzone.com:8181/audio/demo.mp3', 'audio/mp4')
mc.block_until_active()
print(mc.status)
mc.play()

