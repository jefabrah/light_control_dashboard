from phue import Bridge


class LightController():

    def __init__(self, config):
        self.config = config
        self.bridge = Bridge(config.get('ip'))
        self.bridge.connect()
        self.lights = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def set_all_lights_on(self):
        new_light_state = {'transitiontime': 30, 'on': True, 'bri': 254, 'sat': 0}
        self.bridge.set_light(self.lights, new_light_state)

    def set_all_lights_off(self):
        new_light_state = {'transitiontime': 30, 'on': False, 'bri': 254, 'sat': 0}
        self.bridge.set_light(self.lights, new_light_state)

    def set_all_lights_dim(self):
        new_light_state = {'transitiontime': 30, 'on': True, 'bri': 100, 'sat': 0}
        self.bridge.set_light(self.lights, new_light_state)

    def get_all_lights(self):
        return self.bridge.lights