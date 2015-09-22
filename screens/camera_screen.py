from kivy.uix.camera import Camera
from screens_templates import ScreenTmplt
from buttons import buttons


class CameraScreen(ScreenTmplt):

    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.add_widget(Camera(play=True, resolution=(320, 240)))
        self.add_widget(buttons.PipButton(upper=True,
                                          text=self.name.upper(),
                                          size_hint=(0, 0),
                                          size=(50, 20),
                                          pos=(25, 215)))
