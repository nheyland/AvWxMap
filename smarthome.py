import pywemo


class Plug:
    def __init__(self):
        self.url = pywemo.setup_url_for_address("192.168.0.35", None)
        pass

    def toggle(self):
        device = pywemo.discovery.device_from_description(self.url)
        device.toggle()
