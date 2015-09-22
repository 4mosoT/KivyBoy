from kivy.uix.button import Button
from kivy.graphics import Line, Color
from kivy.utils import get_color_from_hex


# Button for screen change
class PipButton(Button):
    # We can choose if the button is selected or not, and if we can draw de
    # side lines

    def __init__(self, upper=False, draw_lines=True, selected=False, **kwargs):
        super(PipButton, self).__init__(**kwargs)
        self.press = False
        self.selected = selected
        self.upper = upper
        if 'screenmanager' in kwargs:
            self.screenmanager = kwargs['screenmanager']
        if 'screen' in kwargs:
            self.screen = kwargs['screen']
            self.press = True
        self.selected = selected
        self.draw_lines = draw_lines
        self.color = get_color_from_hex("#64FEB5")
        # The last item of the array indicates "opacity". '0' is transparent
        if selected:
            self.background_color = [100 / 256., 254 / 256., 181 / 256., .5]
        else:
            self.background_color = [1, 1, 1, 0]
        self.font_name = 'monofonto.ttf'
        self.font_size = "13sp"

        with self.canvas:
            Color(100 / 256., 254 / 256., 181 / 256.)
            if selected:
                self.linea = Line(width=1.3,
                                  rectangle=(self.x, self.y,
                                             self.width, self.height))
            if draw_lines:
                # Left line
                self.linea2 = Line(width=1.3,
                                   points=[self.x - 17,
                                           self.height / 2 + self.y,
                                           self.x - 5,
                                           self.height / 2 + self.y])
                # Right line
                self.linea3 = Line(width=1.3,
                                   points=[self.x + self.width + 17,
                                           self.height / 2. + self.y,
                                           self.x + self.width + 5,
                                           self.height / 2. + self.y])

            if upper:
                aux = 0
                for x in range(1, 9):
                    Color(100 / 256., 254 / 256., 181 / 256., .9 - x / 10.)
                    Line(width=1.3,
                         points=[self.x + self.width + 17,
                                 self.height / 2. + self.y - aux,
                                 self.x + self.width + 17,
                                 self.height / 2. + self.y - aux - 5])
                    aux += 2

    def on_press(self, *args):
        super(PipButton, self).on_press(*args)
        if self.press:
            self.screenmanager.current = self.screen
