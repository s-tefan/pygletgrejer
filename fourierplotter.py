import cmath
import numpy.fft
import time
import pyglet

pi2i = 2*cmath.pi*1j

class FourierPlotter:
    def __init__(self, flist=[]):
        self.flist = flist
        self.mode = None
        self.freq = 1/20
    
    def termlist(self, t):
        n = len(self.flist)
        return [cmath.exp(pi2i*((k+(n//2))%n-(n//2))*self.freq*t)*self.flist[k] \
            for k in range(n)]
    
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
    # Animates the Fourier Series i a FourierPlotter object
    # as a train of phasors in the complex plane

    def __init__(self, width = 1280, height = 720):
        self.fplotters = []
        self.starttime = time.time()
        self.win = pyglet.window.Window(width,height)
        self.win.on_draw = self.on_draw
        self.batch = pyglet.graphics.Batch()
        self.set_axes(1,0,0)

    def add_fplotter(self, fplotter):
        self.fplotters.append(fplotter)

    def set_axes(self, scale=None, xoffset=None, yoffset=None):
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
        t = time.time() - self.starttime
        for fplotter in self.fplotters:
            vlist = []
            zlist = fplotter.hands_vertexlist(t)
            n = len(zlist)
            while zlist:
                z = zlist.pop(0)
                vlist.append(z.real*self.scale+self.xoffset)
                vlist.append(z.imag*self.scale+self.yoffset)
            pyglet.graphics.vertex_list(n,
                ('v2f', vlist),
                ('c3B', (255,0,0)*n) ).draw(pyglet.gl.GL_LINE_STRIP)
        self.batch.draw() # Ritas inget?


    def update(self, dt):
        pass

    def scalez(self, z):
        return z.real*self.scale+self.xoffset, z.imag*self.scale+self.yoffset

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()


class FourierGraph:
    # To plot the graph of the real part
    # To be implemented
    pass

fp = FourierPlotter()
points = (
    cmath.rect(1,0),
    cmath.rect(1,cmath.pi/4),
    cmath.rect(1,cmath.pi/2),
    cmath.rect(0.5,cmath.pi))
fp.setpoints(points)
plist = [1,1+0.25j,1+0.5j,1+0.75j, 
    1+1j,0.75+1j,0.5+1j,0.25+1j,0+1j,-0.25+1j,-0.5+1j,-0.75+1j,
    -1+1j,-1+0.75j,-1+0.5j,-1+0.25j,-1+0j,-1-0.25j,-1-0.5j,-1-0.75j,
    -1-1j,-0.75-1j,-0.5-1j,-0.25-1j,0-1j,0.25-1j,0.5-1j,0.75-1j,
    1-1j,1-0.75j,1-0.5j,1-0.25j] # 32 element från en kvadrat
fp2 = FourierPlotter()
fp2.setpoints(plist)
fa = FourierAnimator()
plist = []
for z in points:
    plist += fa.scalez(z)
print(plist)

fa.batch.add(len(points), 
            pyglet.gl.GL_LINE_STRIP,
            None, 
            ('v2f', plist),
            ('c3B', (0,255,0)*len(points)))

fa.set_axes(200,640,360)
fa.add_fplotter(fp)
fa.add_fplotter(fp2)
print(fa.starttime,fa.fplotters,fa.batch)
fa.run()




