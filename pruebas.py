from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import BorderImage


class MyApp(App):
    def build(self):
        root = Widget()
        b = Button(center=(200, 200), background_color = [0,0,0,0])
        root.add_widget(b)
        with b.canvas.before:
            BorderImage(
                size=(b.width + 100, b.height + 100),
                pos=(b.x - 50, b.y - 50),
                border=(10, 10, 10, 10),
                )

        return root


MyApp().run()
