from kivy.uix.button import Button
from kivy.graphics import Line, Color
from kivy.utils import get_color_from_hex
from  kivy.properties import ObjectProperty, StringProperty

#Main Button
class PipButton(Button):
    screenmanager = ObjectProperty()
    screen = StringProperty()
    #We can choose if the button is selected or not, and if we can draw de side lines
    def __init__(self, draw_lines = True,selected = False, **kwargs):
        super(PipButton, self).__init__(**kwargs)
        if 'screenmanager' in kwargs:
            self.screenmanager= kwargs['screenmanager']
        if 'screen' in kwargs:
            self.screen= kwargs['screen']
        self.selected = selected
        self.draw_lines = draw_lines
        self.color = get_color_from_hex("#64FEB5")
        #The last item of the array indicates "opacity". '0' is transparent
        if selected:
            self.background_color = [100/256., 254/256., 181/256.,.5]
        else:
            self.background_color = [1,1,1,0]
        self.font_name = 'monofonto.ttf'
        self.font_size = "13sp"
        self.bind(size=self.update, pos=self.update)
        with self.canvas.before:
            Color(100/256., 254/256., 181/256.)
            if selected:
                self.linea= Line( rectangle=(self.x, self.y, self.width, self.height), width=1.3)
            if self.draw_lines:
                self.linea2 = Line(width=1.3, points=[self.x - 17, self.height/2 + self.y, self.x - 5, self.height/2 +  self.y])
                self.linea3 = Line(width=1.3, points=[self.x + self.width + 17, self.height/2.+ self.y,self.x + self.width + 5, self.height/2. + self.y])


    def update(self, *args):
        self.linea.rectangle = (self.x,self.y ,self.width, self.height)
        if self.draw_lines:
            self.linea2.points = [self.x - 17, self.height/2 + 1 + self.y, self.x - 5, self.height/2 + 1 +self.y]
            self.linea3.points = [self.x + self.width + 17, self.height/2 + 1 + self.y,self.x + self.width + 5, self.height/2 + 1 +self.y]


    def on_press(self, *args):
        super(PipButton, self).on_press(*args)
        if self.screen:
            self.screenmanager.current = self.screen


