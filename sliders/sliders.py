from kivy.uix.slider import Slider
from kivy.graphics import Color, Rectangle
from kivy.metrics import sp
class PipSlider(Slider):
    def __init__(self, **kwargs):
        super(PipSlider, self).__init__(**kwargs)
        self.bind(value=self.update)

        with self.canvas:
            Color(100 / 256., 254 / 256., 181 / 256.)
            self.rectangle= Rectangle(size=(16,16), pos=(self.center_x - 8 , self.value_pos[1]))



    def update(self, *kwargs):
        self.rectangle.pos = (self.value_pos[0] - 8, self.value_pos[1])


