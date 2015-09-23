from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

from screens.map_screen import Map
from screens.stats_screen import Stats
from screens.control_screen import Control

# Colores: #64FEB5 #005A21


class Manager(ScreenManager):

    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)


class MainApp(App):

    def build(self):
        root = Manager(transition=NoTransition())
        stats = Stats(name='stats')
        map = Map(name='map')
        control = Control(name='control')
        root.add_widget(stats)
        root.add_widget(map)
        root.add_widget(control)

        return root


if __name__ == '__main__':
    MainApp().run()
