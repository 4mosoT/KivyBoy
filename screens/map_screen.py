from kivy.uix.image import AsyncImage

from screens_templates import ScreenTmplt
from buttons import buttons

MAP_URL_TMPL = 'https://maps.googleapis.com/maps/api/staticmap'\
    '?size=295x190&zoom={zoom}&center={lat},{long}'\
    '&style=|color:0x000000'\
    '&style=feature:road|color:0x0E4B29'\
    '&style=feature:all|element:labels|color:0x64FEB5|visibility:off'


class Map(ScreenTmplt):

    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.lat = 40.714728
        self.long = -73.998672
        self.zoom = 13

        self.g_image = AsyncImage(source=MAP_URL_TMPL.format(lat=self.lat,
                                                             long=self.long,
                                                             zoom=self.zoom))

        self.add_widget(self.g_image)
        self.add_widget(buttons.PipButton(text=self.name.upper(),
                                          size_hint=(0, 0),
                                          size=(50, 20),
                                          pos=(25, 215)))

        zoom_in_button = buttons.PipButton(selected=True,
                                           text="Zoom In",
                                           size_hint=(0, 0),
                                           size=(60, 18),
                                           pos=(100, 216))
        zoom_in_button.bind(on_release=self.zoom_in)
        self.add_widget(zoom_in_button)

        zoom_out_button = buttons.PipButton(selected=True,
                                            text="Zoom Out",
                                            size_hint=(0, 0),
                                            size=(60, 18),
                                            pos=(180, 216))
        zoom_out_button.bind(on_release=self.zoom_out)
        self.add_widget(zoom_out_button)

        self.add_widget(buttons.PipButton(text=self.name.upper(),
                                          size_hint=(0, 0),
                                          size=(50, 20),
                                          pos=(25, 215)))

    def update_map(self, *args):
        self.g_image.source = MAP_URL_TMPL.format(lat=self.lat,
                                                  long=self.long,
                                                  zoom=self.zoom)

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
