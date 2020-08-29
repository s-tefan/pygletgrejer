from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle


class TreGrej(Widget):
    apa=0

    def update(self, dt):
        with self.canvas:
            # Add a red color
            Color(1., 0, 0)

            # Add a rectangle
            Rectangle(pos=(10+self.apa, 10+self.apa), size=(100, 100))
            self.apa += 1
            
class TreApp(App):
    def build(self):
        grej = TreGrej()
        Clock.schedule_interval(grej.update, 1.0 / 60.0)
        #grej.update(0)
        return grej


if __name__ == '__main__':
    TreApp().run()