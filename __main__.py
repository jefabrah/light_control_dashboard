import sys
from tkinter import *
from tkinter import ttk

from config import CONFIG
from light_controller import LightController


class App:

    def __init__(self, config):
        self._config = config
        self.window = Tk()
        self._lights = LightController(self._config['lights'])
        self.window.title('Lighting Dashboard')
        self._light_slider = ttk.Scale(self.window, variable=self._lights.brightness,
                                   command=self._lights.set_all_lights_brightness,
                                   orient=HORIZONTAL, from_=0, to=254, len=600)
        self._light_slider.grid(row=0, column=1, sticky=W+E)
        self.window.geometry('800x480')

    def main(self):
        self.init_light_controller()
        self.init_window()

    def init_light_controller(self):
        lights = self._lights.get_all_lights()
        print('Initialized light controller')

    def init_window(self):
        self.window.mainloop()

    def exit(self, reason):
        print(f'Exiting app because: {reason}')
        exit()


if __name__ == '__main__':
    app = App(CONFIG)
    app.main()