from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, NoTransition
from screens import ScreenTmplt
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
from kivy.uix.camera import Camera

import psutil
import labels
import buttons

# Colores: #64FEB5 #005A21

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)


class Stats(ScreenTmplt):
    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)
        self.add_widget(
            buttons.PipButton(upper=True, text=self.name.upper(), size_hint=(0, 0), size=(50, 20), pos=(25, 215)))
        # Call update func every .5 secs
        Clock.schedule_interval(self.update, 0.5)
        # Read use of RAM and set text label
        self.ram = labels.PipLabel(size_hint=(0, 0), size=(20, 20), pos=(135, 205), gradient=True)
        self.add_widget(labels.PipLabel(text='RAM', size_hint=(0, 0), size=(30, 20), pos=(100, 205)))
        self.add_widget(self.ram)

        with self.canvas.after:
            Rectangle(source='images/tboy.gif', size_hint=(0, 0), pos=(100, 80))

    def update(self, *args):
        memory = psutil.virtual_memory().percent
        self.ram.text = str(memory)


class Objects(ScreenTmplt):
    def __init__(self, **kwargs):
        super(Objects, self).__init__(**kwargs)
        self.add_widget(
            buttons.PipButton(upper=True, text=self.name.upper(), size_hint=(0, 0), size=(50, 20), pos=(25, 215)))
        self.add_widget(Camera(play=True, resolution=(320,240)))

class Map(ScreenTmplt):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)

        self.lat = 40.714728
        self.long = -73.998672
        self.zoom = 13

        self.g_image = AsyncImage(
            source='https://maps.googleapis.com/maps/api/staticmap?size=295x190&zoom=13&center=' + str(
                self.lat) + ',' + str(self.long) + '&style=|color:0x000000'
                                                   '&style=feature:road|color:0x0E4B29'
                                                   '&style=feature:all|element:labels|color:0x64FEB5|visibility:off'
            )

        self.add_widget(self.g_image)
        self.add_widget(buttons.PipButton(text=self.name.upper(), size_hint=(0, 0), size=(50, 20), pos=(25, 215)))

        zoom_in_button = buttons.PipButton(selected=True, text="Zoom In", size_hint=(0, 0), size=(60, 18),
                                           pos=(100, 216))
        zoom_in_button.bind(on_release=self.zoom_in)
        self.add_widget(zoom_in_button)

        zoom_out_button = buttons.PipButton(selected=True, text="Zoom Out", size_hint=(0, 0), size=(60, 18),
                                            pos=(180, 216))
        zoom_out_button.bind(on_release=self.zoom_out)
        self.add_widget(zoom_out_button)

        self.add_widget(buttons.PipButton(text=self.name.upper(), size_hint=(0, 0), size=(50, 20), pos=(25, 215)))

    def update_map(self, *args):
        self.g_image.source = 'https://maps.googleapis.com/maps/api/staticmap?size=295x190&zoom=' + str(
            self.zoom) + '&center=' + str(self.lat) + ',' + str(
            self.long) + '&style=|color:0x000000&style=feature:road|color:0x0E4B29&style=feature:all|element:labels|color:0x64FEB5|visibility:off'

    def zoom_in(self, *args):
        self.zoom += 1
        self.update_map()

    def zoom_out(self, *args):
        self.zoom -= 1
        self.update_map()

    def on_touch_up(self, touch):

        x = touch.x
        y = touch.y

        z = self.zoom

        if 11 <= x <= 55 and 60 <= y <= 190:
            self.long -= 0.005
        if 260 <= x <= 300 and 60 <= y <= 190:
            self.long += 0.005
        if 91 <= x <= 250 and 170 <= y <= 206:
            self.lat += 0.005
        if 91 <= x <= 250 and 30 <= y <= 80:
            self.lat -= 0.005
        self.update_map()


class MainApp(App):
    def build(self):
        root = Manager(transition=NoTransition())
        stats = Stats(name='stats')
        map = Map(name='map')
        objects = Objects(name='objects')
        root.add_widget(stats)
        root.add_widget(map)
        root.add_widget(objects)

        return root


if __name__ == '__main__':
    MainApp().run()
