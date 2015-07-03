import kivy.uix.label
from kivy.utils import get_color_from_hex
from kivy.graphics import Line, Color


class PipLabel(kivy.uix.label.Label):
    def __init__(self, gradient=False, **kwargs):
        super(PipLabel, self).__init__(**kwargs)
        self.font_name = 'monofonto.ttf'
        self.font_size = "13sp"
        self.background_color = [1, 1, 1, 0]
        self.color = get_color_from_hex("#64FEB5")
        with self.canvas.before:
            Color(100 / 256., 254 / 256., 181 / 256.)
            Line(width=1.3, points=[self.x - 3, self.height + self.y, self.x + self.width + 6, self.height + self.y])
            if gradient:
                aux = 0
                for x in range(1, 9):
                    Color(100 / 256., 254 / 256., 181 / 256., .9 - x / 10.)
                    Line(points=[self.x + self.width + 6, self.height + self.y - aux, self.x + self.width + 6,
                                 self.height + self.y - aux - 2], width=1.3)
                    aux += 2
