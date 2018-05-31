import sys
from config import CONFIG
from LightController import LightController


class App():

    def __init__(self, config):
        self.config = config

    def main(self):
        self.lights = LightController(self.config.get('lights'))
        self.init_light_controller()

    def init_light_controller(self):
        self.lights.set_all_lights_dim()


if __name__ == '__main__':
    app = App(CONFIG)
    app.main()