    #!/usr/bin/env python
import pyglet
import math


def sinus_curve(x0,y0,length,amp):
    n_points = 101
    step = 2*math.pi/(n_points-1)
    vlist = []
    clist = []
    color = [255,0,0]
    for k in range(n_points):
        t=k*step
        x = x0 + int(length * k / n_points)
        y = y0 + int(amp*math.sin(t))
        vlist += [x,y]
        clist += color
    return pyglet.graphics.vertex_list(n_points, 
            ('v2i',vlist),
            ('c3B',clist)
        )
    

window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()
    burgaren.blit(0,0)
    label.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
        ('v2i', (10, 15, 30, 35)))
    vlist0.draw(pyglet.gl.GL_TRIANGLE_STRIP)
    vlist1.draw(pyglet.gl.GL_QUADS)
    scurve.draw(pyglet.gl.GL_LINE_STRIP)
        
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (100, 100,
             150, 100,
             150, 150,
             100, 150))
    )

@window.event
def on_key_press(symbol, modifiers):
    print('A key', str(symbol), 'was pressed')
    if symbol==pyglet.window.key.G:
        vlist1.colors[9:]=[0,255,0]
    elif symbol==pyglet.window.key.B:
        vlist1.colors[9:]=[0,0,255]
    elif symbol==pyglet.window.key.R:
        vlist1.colors[9:]=[255,0,0]
    elif symbol==pyglet.window.key.K:
        vlist1.colors[9:]=[0,0,0]
    elif symbol==pyglet.window.key.W:
        vlist1.colors[9:]=[255,255,255]



label = pyglet.text.Label('Hello, world!',
                          font_name='Arial',
                          font_size=36,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')

burgaren = pyglet.resource.image('burgare.jpg')

vlist0 = pyglet.graphics.vertex_list(4, 
        ('v2i', (200, 100,
             250, 100,
             250, 150,
             200, 150)),
        ('c3B', (0,0,0,
            255,255,255,
            255,0,0,
            0,0,255))
    )

vlist1 = pyglet.graphics.vertex_list(4, 
        ('v2i', (300, 100,
             350, 100,
             350, 150,
             300, 150)),
        ('c3B', (0,0,0,
            255,255,255,
            255,0,0,
            0,0,255))
    )

scurve = sinus_curve(10,300,300,100)


pyglet.app.run()
