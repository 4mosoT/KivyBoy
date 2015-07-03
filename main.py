from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, NoTransition
from screens import ScreenTmplt
from kivy.clock import Clock
import psutil
import labels

# Colores: #64FEB5 #005A21

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)


class Stats(ScreenTmplt):
    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)

        # Call update func every .5 secs
        Clock.schedule_interval(self.update, 0.5)

        # Read use of RAM and set text label
        self.ram = labels.PipLabel(size_hint=(0, 0), size=(20, 20), pos=(135, 205), gradient=True)
        self.add_widget(labels.PipLabel(text='RAM', size_hint=(0, 0), size=(30, 20), pos=(100, 205)))
        self.add_widget(self.ram)

        with self.canvas.before:
            Rectangle(source='images/tboy.gif', size_hint=(0, 0), pos=(100, 80))

    def update(self, *args):
        memory = psutil.virtual_memory().percent
        self.ram.text = str(memory)


class Objects(ScreenTmplt):
    def __init__(self, **kwargs):
        super(Objects, self).__init__(**kwargs)


class Skills(ScreenTmplt):
    def __init__(self, **kwargs):
        super(Skills, self).__init__(**kwargs)


class MainApp(App):
    def build(self):
        root = Manager(transition=NoTransition())
        stats = Stats(name='stats')
        skills = Skills(name='skills')
        objects = Objects(name='objects')
        root.add_widget(stats)
        root.add_widget(skills)
        root.add_widget(objects)

        return root


if __name__ == '__main__':
    MainApp().run()
