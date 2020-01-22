import math
import numpy as np
import pyglet
from pyglet.gl import *

class Cube:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(8, 
            ('v3f', (1,1,1, -1,1,1, -1,-1,1, 1,-1,1,
                    1,1,-1, -1,1,-1, -1,-1,-1, 1,-1,-1)), 'c4B')
        
        self.cubebatch = pyglet.graphics.Batch()
        cfa = self.cubebatch.add_indexed(4,pyglet.gl.GL_POLYGON,None,[0,1,2,3], self.vertices)
        cfb = self.cubebatch.add_indexed(4,pyglet.gl.GL_POLYGON,None,[7,6,5,4], self.vertices)
        cfc = self.cubebatch.add_indexed(4,pyglet.gl.GL_POLYGON,None,[0,3,7,4], self.vertices)
        cfd = self.cubebatch.add_indexed(4,pyglet.gl.GL_POLYGON,None,[0,4,5,1], self.vertices)
        cfe = self.cubebatch.add_indexed(4,pyglet.gl.GL_POLYGON,None,[1,5,6,2], self.vertices)
        cff = self.cubebatch.add_indexed(4,pyglet.gl.GL_POLYGON,None,[2,6,7,3], self.vertices)
        self.faces = [cfa,cfb,cfc,cfd,cfe,cff]

class Animator:
    def __init__(self):
        width = 1200
        height = 800
        self.win = pyglet.window.Window(width,height)
        self.cube = Cube()
        self.win.on_draw = self.on_draw

    #@win.event
    def on_draw():
        self.cube.cubebatch.draw()


a = Animator()
pyglet.app.run()
