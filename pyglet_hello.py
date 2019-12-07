#!/usr/bin/env python
import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world!',
                          font_name='Arial',
                          font_size=36,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')

burgaren = pyglet.resource.image('burgare.jpg')


@window.event
def on_draw():
    window.clear()
    burgaren.blit(0,0)
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')


pyglet.app.run()
