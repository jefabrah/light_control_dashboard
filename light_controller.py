from phue import Bridge
import tkinter as tk
from debounce import  debounce


class LightController:

    def __init__(self, config):
        self.config = config
        self.bridge = Bridge(config.get('ip'))
        self.bridge.connect()
        self._lights = self.bridge.get_light_objects('id')
        self.brightness = tk.IntVar

    def set_all_lights_on(self):
        new_light_state = {'transitiontime': 30, 'on': True, 'bri': 254, 'sat': 0}
        self.bridge.set_light(self._lights, new_light_state)

    def set_all_lights_off(self):
        new_light_state = {'transitiontime': 30, 'on': False, 'bri': 254, 'sat': 0}
        self.bridge.set_light(self._lights, new_light_state)

    @debounce(0.5)
    def set_all_lights_brightness(self, brightness):
        bri = round(int(float(brightness)))
        new_light_state = {'transitiontime': 0, 'on': True, 'bri': bri}
        self.bridge.set_light(self._lights, new_light_state)
        self.brightness = brightness
        print(f'brightness: {brightness}')

    def get_all_lights(self):
        return self._lights
