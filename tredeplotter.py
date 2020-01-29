import math
import numpy as np
import pyglet
from pyglet.gl import *


class PlotWindow(pyglet.window.Window):
    def __init__(self):
        super(PlotWindow, self).__init__()
        self.drawn = False
        batch = None

    def on_draw(self):
        # clear the screen
        #glClear(GL_COLOR_BUFFER_BIT)
        # vi kör den här istället
        #win.clear()
        #if not self.drawn:
        if True:
            self.batch.draw()
            print("Ritar!")
            self.drawn = True
        pyglet.graphics.vertex_list(2,('v3f',(-1,-1,-1,1,1,1)),('c3b',(1,0,0,0,0,1))).draw(pyglet.gl.GL_LINES)
        # funkar inte efter subklassningen


    def on_resize(self, width, height):
        print("Resize")
        self.drawn = False

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
        self.batch.draw()

    def on_activate(self):
        print("Activated!")




def mesh(fun):
    xmin, xmax, ymin, ymax = -1, 1, -1, 1
    #dx, dy = 0.1, 0.1
    #nx, ny = 1+int((xmax-xmin)//dx), 1+int((ymax-ymin)//dy)
    nx = 5
    ny = 5
    dx = (xmax-xmin)/(nx-1)
    dy = (ymax-ymin)/(ny-1)
    vlist = []
    quadlist = []
    linelist = []
    n = 0
    for ky in range(ny):
        y = ymin + ky*dy 
        for kx in range(nx):
            x = xmin + kx*dx 
            vlist += [x, y, fun(x,y)]
            if kx > 0:
                linelist += [n-1,n]
            if ky > 0:
                linelist += [n-nx,n]
                if kx > 0:
                    quadlist += [n-nx-1, n-nx, n, n-1]
            n += 1
    return vlist, linelist, quadlist

def meshbatch():
    vlist, linelist, quadlist = mesh(lambda x,y : 1)
    ba = pyglet.graphics.Batch()
    ba.add_indexed(len(vlist)//3, pyglet.gl.GL_LINES, None, linelist,
        ('v3f', vlist))
    return ba




print(mesh(lambda x,y : 1))


win = PlotWindow()
win.batch = meshbatch()

@win.event


pyglet.app.run()
