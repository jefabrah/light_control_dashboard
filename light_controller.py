import tkinter as tk

from phue import Bridge

from throttle import throttle


class LightController:

    def __init__(self, config):
        self.config = config
        self.bridge = Bridge(config.get('ip'))
        self.bridge.connect()
        self._lights = self.bridge.get_light_objects('id')
        self.brightness = tk.IntVar
        self._lights_on = self.are_all_lights_on()

    def set_all_lights_on(self, on=True):
        new_light_state = {'transitiontime': 10, 'on': on, 'bri': 254, 'sat': 0}
        self.bridge.set_light(self._lights, new_light_state)
        self._lights_on = True

    def set_all_lights_brightness(self, brightness):
        bri = round(int(float(brightness)))
        if bri < 1:
            self.set_all_lights_on(False)
            self.brightness = 0
            return False

        new_light_state = {'transitiontime': 0, 'on': True, 'bri': bri}
        self.bridge.set_light(self._lights, new_light_state)
        self.brightness = brightness
        return True

    def get_all_lights(self):
        return self._lights

    def are_all_lights_on(self):
        for light in self.bridge.get_light_objects():
            if not light.on:
                return False
        return True

    def sync_lights(self):
        self._lights_on = self.are_all_lights_on()

    @throttle(seconds=3)
    def toggle_all_lights(self, window):
        on = not self.are_all_lights_on()
        self.set_all_lights_on(on)
        button_text = 'OFF' if on else 'ON'
        window._power_button['text'] = button_text
        window._lights.sync_lights()
        window.sync_window()
