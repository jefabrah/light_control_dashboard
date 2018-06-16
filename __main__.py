from threading import Thread
from tkinter import *
from tkinter import ttk

from config import CONFIG
from debounce import debounce
from light_controller import LightController


class App:

    def __init__(self, config):
        self._config = config
        self.window = Tk()
        self.window.title('Lighting Dashboard')
        self._lights = LightController(self._config['lights'])
        self._light_slider = ttk.Scale(self.window, variable=self._lights.brightness,
                                       command=self.slider_change,
                                       orient=HORIZONTAL, from_=0, to=254, len=600)

        self._power_button = ttk.Button(
            self.window, text="OFF", command=self.handle_toggle_all_lights)

        self._power_button.grid(row=1, column=1, rowspan=3, padx=(50, 50),
                                pady=(50, 50), sticky=N + S + W + E)
        self._light_slider.grid(
            row=0, column=1, padx=(100, 100), pady=(50, 50))
        self.window.geometry('800x480')

    def handle_toggle_all_lights(self):
        self._lights.toggle_all_lights(self)

    def main(self):
        self.init_window()

    def init_window(self):
        self.sync_window()
        self.window.mainloop()

    def sync_window(self):
        button_text = 'OFF' if self._lights.are_all_lights_on() else 'ON'
        self._power_button['text'] = button_text
        brightness = 254 if self._lights.are_all_lights_on() else 0
        if (brightness > 0 or brightness < 254) or self._lights.brightness == brightness:
            return
        if brightness == 0:
            self._lights.set_all_lights_on(False)

    @debounce(0.5)
    def slider_change(self, brightness):
        print(f'Brightness:{brightness}')
        thread = Thread(
            target=self._lights.set_all_lights_brightness, args=(brightness,))
        on = self._lights.set_all_lights_brightness(brightness)
        self._power_button['text'] = 'OFF' if on else 'ON'
        thread.start()

    @staticmethod
    def exit(reason):
        print(f'Exiting app because: {reason}')
        exit()


if __name__ == '__main__':
    app = App(CONFIG)
    app.main()
