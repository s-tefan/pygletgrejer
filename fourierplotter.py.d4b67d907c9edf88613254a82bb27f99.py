import cmath
import numpy.fft
import time
import pyglet

pi2i = 2*cmath.pi*1j

class FourierPlotter:
    def __init__(self, flist=[]):
        self.flist = flist
        self.mode = None
        self.omega = 1
    
    def termlist(self, t):
        n = len(flist)
        return [exp(pi2i*((k+(n//2))%n-(n//2))*t)*self.flist[k] for k in range(n)]
    
    def setpoints(self, plist):
        flistraw = numpy.fft.fft(plist)
        n = len(flistraw)
        self.flist = [f/n for f in flistraw]

    def set_mode(mode):
        self.mode = mode
    
    def start(self):
        self.starttime = time.time()
    
    def hands_vertexlist(self, t, mode=0):
        tlist = self.termlist(t)
        n = len(tlist)
        if self.mode == 1:
            # lowest frequency first, sum of counterclockwise and clockwise, 
            z = tlist[0]
            zlist = [z]
            for k in range(1,n//2): #?
                z += tlist[k]+tlist[-k]
                zlist.append(z)
            if n%2:
                z += tlist[n//2]
                zlist.append(z)
        else:
            # lowest frequency first, counterclockwise, clockwise, 
            z = tlist[0]
            zlist = [z]
            for k in range(1,n//2): #?
                z += tlist[k]
                zlist.append(z)
                z += tlist[-k]
                zlist.append(z)
            if n%2:
                z += tlist[n//2]
                zlist.append(z)
        return zlist

class FourierAnimator:

    def __init__(self, width = 1280, height = 720):
        fplotters = []
        self.starttime = time.time()
        self.win = pyglet.window.Window(width,height)
        self.win.on_draw = self.on_draw
    def add_fplotter(self, fplotter, scale = 1, xoffset = 0, yoffset = 0):
        pass
    def set_axes(self, scale=None,xoffset=None,yoffset=None):
        if scale != None: self.scale = scale
        if xoffset != None: self.xoffset = xoffset
        if yoffset != None: self.yoffset = yoffset

    def on_draw(self):
        self.win.clear()
        g = pyglet.graphics.vertex_list(
            5,
            ('v2f', [650,360,640,350,630,360,640,370,650,360]),
            ('c3B', (255,0,0)*5))
        g.draw(pyglet.gl.GL_LINE_STRIP)

        for fplotter in self.fplotters:
            vlist = []
            zlist = fplotter.hands_vertexlist(0)
            n = zlist
            while zlist:
                z = zlist.pop(0)
                vlist.append(z.real*scale+xoffset)
                vlist.append(z.imag*scale+yoffset)
            pyglet.graphics.vertex_list(n,
                ('v2f', vlist),
                ('c3B', (255,0,0)*n) ).draw(pyglet.gl.GL_LINE_STRIP)




    def run(self):
        pyglet.app.run()

fp = FourierPlotter()
fp.setpoints((cmath.rect(1,0),cmath.rect(1,cmath.pi/4),cmath.rect(1,cmath.pi/2),cmath.rect(0.5,cmath.pi)))
fa = FourierAnimator()
fa.set_axes(200,640,360)
fa.add_fplotter(fp)
fa.run()




