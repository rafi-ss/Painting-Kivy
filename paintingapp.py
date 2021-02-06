from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Ellipse, Line , Color
from kivy.properties import ListProperty , NumericProperty

import random

Window.size = (500, 700)

class PaintingWidget(Widget):

    current_rgb_color = ListProperty([0,0,0])
    current_width = NumericProperty(0)

    def on_touch_down(self, touch):
        super(PaintingWidget, self).on_touch_down(touch)

        if self.collide_point(*touch.pos):

            self.canvas.add(Color(*self.current_rgb_color))
            self.line = Line(points = (touch.pos[0], touch.pos[1]) , width = self.current_width )
            self.canvas.add(self.line)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.line.points  += [touch.pos[0], touch.pos[1]]


class MainLayout(BoxLayout):
    pass


class PaintingApp(App):

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    PaintingApp().run()