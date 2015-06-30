from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, NoTransition
from screens import ScreenTmplt
from  kivy.uix.label import Label

#Colores: #64FEB5 #005A21

class Manager(ScreenManager):

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)


class Stats(ScreenTmplt):

    def __init__(self, *args, **kwargs):
        super(Stats, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        super(Stats, self).on_pre_enter(*args)
        with self.canvas.before:
            Rectangle(source='images/tboy.gif',size_hint=(0,0),pos=(100,80))

class PiObjects(ScreenTmplt):

    def __init__(self, *args, **kwargs):
        super(PiObjects, self).__init__(**kwargs)


class Skills(ScreenTmplt):

    def __init__(self, *args, **kwargs):
        super(Skills, self).__init__(**kwargs)



class MainApp(App):

    def build(self):
        root=Manager(transition=NoTransition())
        stats = Stats(name='stats')
        skills = Skills(name='skills')
        objects = PiObjects(name='objects')
        root.add_widget(stats)
        root.add_widget(skills)
        root.add_widget(objects)
        stats.on_pre_enter()

        return root



if __name__ == '__main__':
    MainApp().run()