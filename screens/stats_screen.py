from kivy.graphics import Rectangle
from kivy.clock import Clock
import psutil

from screens_templates import ScreenTmplt
from buttons import buttons
from labels import labels


class Stats(ScreenTmplt):

    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)
        self.add_widget(buttons.PipButton(upper=True,
                                          text=self.name.upper(),
                                          size_hint=(0, 0),
                                          size=(50, 20),
                                          pos=(25, 215)))
        # Call update func every .5 secs
        Clock.schedule_interval(self.update, 0.5)
        # Read use of RAM and set text label
        self.ram = labels.PipLabel(line=True,
                                   size_hint=(0, 0),
                                   size=(20, 20),
                                   pos=(135, 205),
                                   gradient=True)
        self.add_widget(labels.PipLabel(line=True,
                                        text='RAM',
                                        size_hint=(0, 0),
                                        size=(30, 20),
                                        pos=(100, 205)))
        self.add_widget(self.ram)

        with self.canvas.after:
            Rectangle(source='images/tboy.gif',
                      size_hint=(0, 0),
                      pos=(100, 80))

    def update(self, *args):
        memory = psutil.virtual_memory().percent
        self.ram.text = str(memory)
