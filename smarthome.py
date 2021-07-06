import pywemo


class Plug:
    def toggle():
        url = pywemo.setup_url_for_address("192.168.0.35", None)
        device = pywemo.discovery.device_from_description(url)
        device.toggle()
