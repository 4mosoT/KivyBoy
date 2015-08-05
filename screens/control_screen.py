from screens_templates import ScreenTmplt
from sliders.sliders import PipSlider
from buttons.buttons import PipButton
from labels.labels import PipLabel
try:
    import RPi.GPIO as GPIO
except ImportError:
    pass


class Control (ScreenTmplt):
    def __init__(self, **kwargs):
        super(Control, self).__init__(**kwargs)
        self.add_widget(PipButton(upper=True, text=self.name.upper(), size_hint=(0, 0), size=(50, 20), pos=(25, 215)))
        self.slide_1 =PipSlider(range=(-5,5), step=0.1, value = 0,size_hint=(0,0), size=(190,20), pos=(70,50))
        self.label_1 =PipLabel(size=(50,100),size_hint=(0,0),pos=(20, 10),  text=str(self.slide_1.value))
        self.slide_1.bind(value=self.ValueChange)
        self.add_widget(self.slide_1)
        self.add_widget(self.label_1)



    def ValueChange(self, instance,value):
        self.label_1.text = str(self.slide_1.value)
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18, GPIO.OUT)
            p=GPIO.PWM(18, 50)
            p.start(6.9 + self.slide_1.value)
            p.stop()
            GPIO.cleanup()
        except:
            pass
