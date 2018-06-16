from config import CONFIG
from light_controller import LightController
from window import Window


class App:

    def __init__(self, config):
        self._config = config
        self._lights = LightController(self._config['lights'])
        self.window = Window(self._lights)

    @staticmethod
    def main():
        print('App initialized')

    @staticmethod
    def exit(reason):
        print(f'Exiting app because: {reason}')
        exit()


if __name__ == '__main__':
    app = App(CONFIG)
    app.main()
