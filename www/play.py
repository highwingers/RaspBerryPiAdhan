import pychromecast
if __name__ == "__main__":
    cast = pychromecast.get_chromecasts()[0]
    print(cast.device)
    mc = cast.media_controller
    mc.play_media("http://remote.khanzone.com:8181/audio/demo.mp3", content_type = "audio/mp4")
    mc.block_until_active()
    mc.play()

