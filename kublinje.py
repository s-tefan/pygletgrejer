import math
import numpy as np
import pyglet
from pyglet.gl import *

win = pyglet.window.Window()

pts = [0]*360

frame = 0
def update_frame(dt):
    global frame
    if frame == None:
        frame = 0
    else:
        frame += 1
    frame %= len(pts)
    print(frame)

@win.event
def on_draw():
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT)



    glPushMatrix()
    glScalef(1,1,1)
    glRotatef(frame,1,1,1)
    cubebatch.draw()
    glPopMatrix()

@win.event
def on_resize(width, height):
    # set the Viewport
    glViewport(0, 0, width, height)

    # using Projection mode
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    aspectRatio = width / height
    gluPerspective(35, aspectRatio, 1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScalef(100,100,0.1) # scaling i z here changes the clip [-1,1]
    glTranslatef(3, 2, 0) # translate before scaling
    # center is at origin (lower left) so need to translate
    gluLookAt(0.5,1,2, 0,0,0, 0,1,0) # eye, center, up 
    #glRotatef(85,1,0,0)


vertices = ('v3f', (-1,-1,1, 1,-1,1, 1,-1,-1, -1,-1,-1,
                    -1,1,-1, 1,1,-1, 1,1,1, -1,1,1))
colors = ('c4f', (0,0,0,1, 0,0,0,1, 0,0,1,1, 0,0,1,1,
                0.8,0,0.8,0.8, 0.8,0.0,0.8,0.8, 1,0,0,0.8, 1,0,0,0.8))
cubebatch = pyglet.graphics.Batch()
cfa = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[0,1,6,7], vertices, colors)
cfb = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[1,2,5,6], vertices, colors)
cfc = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[2,3,4,5], vertices, colors)
cfd = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[0,7,4,3], vertices, colors)
cfe = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[7,6,5,4], vertices, colors)
cff = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[3,2,1,0], vertices, colors)
faces = [cfa,cfb,cfc,cfd,cfe,cff]
col = ('c3f', (0,0,0)*8)
edges = cubebatch.add_indexed(8,pyglet.gl.GL_LINES,None,
    [0,1, 1,2, 2,3, 3,0, 4,5, 5,6, 6,7, 7,4, 1,6, 2,5, 3,4, 0,7], 
    vertices, col )
cfb = cubebatch.add_indexed(8,pyglet.gl.GL_POLYGON,None,[1,2,5,6], vertices, colors)

vert = ('v3f', (-1, -1, 1,
                1, 1/5, 1,
                1, 1, -1/3,
                3/5, 1, -1,
                -3/5, -1, -1,
                -1, -1, -1/3,
                -1, -1/5 , 1,
                1, 1, 1
))


path = cubebatch.add(8,pyglet.gl.GL_LINE_STRIP,None,vert,col)

# every 1/10 th get the next frame
pyglet.clock.schedule_interval(update_frame, 1/10)
pyglet.app.run()
