import pyglet




vlist = [
    -0.5,   -0.5,   0,
    0.5,    -0.5,   0,
    0,      0.5,    0    ]

win = pyglet.window.Window()
batch = pyglet.graphics.Batch()
pyglet.app.run()


@win.event
def on_draw():
    win.clear()
    pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
        [0,1,2],
        ('v3f', vlist)
    )
