from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Line, Color
from kivy.graphics.instructions import Instruction, InstructionGroup
from kivy.clock import Clock

import buttons


class ScreenTmplt(Screen):
    def __init__(self, **kwargs):
        super(ScreenTmplt, self).__init__(**kwargs)
        with self.canvas.before:
            Color(100 / 256., 254 / 256., 181 / 256.)
            self.rect = Rectangle(source='images/background.png', size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Clock.schedule_interval(self.scanbar, 0.1)
        # self.scanlines = InstructionGroup()
        # self.initial = 0

    def _update_rect(self, instance, *args):

        snames = self.manager.screen_names
        initial_pos = [29, 4]
        for s_screen in snames:
            if self.name == s_screen:
                self.add_widget(
                    buttons.PipButton(selected=True, text=s_screen.capitalize(), size_hint=(0, 0), size=(70, 20),
                                      pos=initial_pos))
                initial_pos[0] += 96
            else:
                self.add_widget(
                    buttons.PipButton(text=s_screen.capitalize(), size_hint=(0, 0), size=(70, 20), pos=initial_pos,
                                      screen=s_screen, screenmanager=self.manager))
                initial_pos[0] += 96

        self.rect.pos = instance.pos
        self.rect.size = instance.size

        with self.canvas.before:
            Line(points=[10, 20, 10, 14], width=1.3)  # Bottom Left
            Line(points=[self.width - 10, 20, self.width - 10, 14], width=1.3)  # Bottom right
            aux = 20
            for x in range(1, 9):
                Color(100 / 256., 254 / 256., 181 / 256., .9 - x / 10.)
                Line(points=[self.width - 10, aux, self.width - 10, aux + 2], width=1.3)  # Gradient bottom right
                Line(points=[self.width - 8, self.height - aux - 5, self.width - 8, self.height + 5 - aux],
                     width=1.3)  # Gradient top right
                Line(points=[self.x + 8, self.height - aux - 5, self.x + 8, self.height + 5 - aux],
                     width=1.3)  # Gradient top left
                Line(points=[10, aux, 10, aux + 2], width=1.3)  # Gradient bottom left
                aux += 2

    def scanbar(self, *args):
        self.scanlines.clear()
        for x in range(0, 5):
            self.scanlines.add(Color(14 / 256., 75 / 256., 41 / 256., .01 + (x / 100.)))
            self.scanlines.add(Line(
                points=[self.x, self.height - 4 * x - self.initial, self.width, self.height - 4 * x - self.initial],
                width=2))

        self.canvas.after.add(self.scanlines)

        self.initial += 5
        if self.initial == 240:
            self.initial = 0
