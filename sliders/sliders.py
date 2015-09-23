from kivy.uix.slider import Slider
from kivy.graphics import Color, Rectangle
from kivy.metrics import sp


class PipSlider(Slider):

    def __init__(self, **kwargs):
        super(PipSlider, self).__init__(**kwargs)
        self.bind(value=self.update)
        self.canvas.clear()
        with self.canvas:

            Color(100 / 256., 254 / 256., 181 / 256., 0.3)
            self.rectangle_background = Rectangle(size=(self.width - self.padding, 1),
                                                  pos=(self.x + self.padding, self.y + self.height / 2.))
            Color(100 / 256., 254 / 256., 181 / 256.)
            self.rectangle_cursor = Rectangle(source="images/piphand2.png",
                                              size=(20, 30),
                                              pos=(self.center_x - 8, self.value_pos[1]))

    def update(self, *kwargs):
        self.rectangle_cursor.pos = (self.value_pos[0] - 8, self.value_pos[1])
