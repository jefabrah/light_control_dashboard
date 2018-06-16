from threading import Thread
from tkinter import *
from tkinter import ttk

from debounce import debounce
from throttle import throttle


class Window:

    def __init__(self, lights):
        self._lights = lights
        self._tk = Tk()
        self._tk.title('Lighting Dashboard')
        self._light_slider = ttk.Scale(self._tk, variable=self._lights.brightness,
                                       command=self.slider_change,
                                       orient=HORIZONTAL, from_=0, to=254, len=600)

        self._power_button = ttk.Button(
            self._tk, text="OFF", command=self.power_button_click)

        self._power_button.grid(row=1, column=1, rowspan=3, padx=(50, 50),
                                pady=(50, 50), sticky=N + S + W + E)
        self._light_slider.grid(
            row=0, column=1, padx=(100, 100), pady=(50, 50))
        self._tk.geometry('800x480')
        self._tk.mainloop()

    @throttle(seconds=3)
    def power_button_click(self):
        on = not self._lights.are_all_lights_on()
        self._lights.set_all_lights_on(on)
        button_text = 'OFF' if on else 'ON'
        self._power_button['text'] = button_text
        self._lights.sync()
        self.sync()

    def sync(self):
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
