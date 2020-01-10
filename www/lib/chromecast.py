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
        return chromecasts
