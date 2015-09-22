from screens_templates import ScreenTmplt
from sliders.sliders import PipSlider
from buttons.buttons import PipButton
from labels.labels import PipLabel
try:
    import pigpio
except ImportError:
    pass


class Control (ScreenTmplt):

    def __init__(self, **kwargs):
        super(Control, self).__init__(**kwargs)
        self.add_widget(PipButton(upper=True,
                                  text=self.name.upper(),
                                  size_hint=(0, 0),
                                  size=(50, 20),
                                  pos=(25, 215)))

        self.slide_1 = PipSlider(range=(-150, 150),
                                 step=10,
                                 value=0,
                                 size_hint=(0, 0),
                                 size=(190, 20),
                                 pos=(70, 50))

        self.label_1 = PipLabel(size=(50, 100),
                                size_hint=(0, 0),
                                pos=(20, 10),
                                text=str(self.slide_1.value))
        self.slide_1.bind(value=self.ValueChange)
        self.add_widget(self.slide_1)
        self.add_widget(self.label_1)

    def ValueChange(self, instance, value):
        self.label_1.text = str(self.slide_1.value)
        try:
            p = pigpio.pi()
            p.set_servo_pulsewidth(18, 1500 + self.slide_1.value)
        except:
            pass
