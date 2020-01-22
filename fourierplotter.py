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
        self.trace = []
        self.tracelen = 1000
    
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

    def add_to_trace(self,z):
        if len(self.trace) >= self.tracelen:
            self.trace.pop(0)
        self.trace.append(z)
    
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
        self.add_to_trace(zlist[-1])
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
        self.phasordict = {}
        self.tracedict = {}

    def add_fplotter(self, fplotter):
        self.fplotters.append(fplotter)

    def set_axes(self, scale=None, xoffset=None, yoffset=None):
        if scale != None: self.scale = scale
        if xoffset != None: self.xoffset = xoffset
        if yoffset != None: self.yoffset = yoffset

    def old_on_draw(self):
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
                ('c3B', (0,255,0)*n) ).draw(pyglet.gl.GL_LINE_STRIP)
            tlist = []
            tlen = len(fplotter.trace)
            for z in fplotter.trace:
                tlist += [z.real*self.scale+self.xoffset,
                    z.imag*self.scale+self.yoffset]
            pyglet.graphics.vertex_list(tlen,
                ('v2f', tlist),
                ('c3B', (255,0,0)*tlen) ).draw(pyglet.gl.GL_LINE_STRIP)
            
        self.batch.draw()
    
    def on_draw(self):
        self.win.clear()
        self.batch.draw()

    def init_graphics(self): # instead of old_on_draw, togeether with update
        g = self.batch.add(5, 
            pyglet.gl.GL_LINE_STRIP, None,
            ('v2f', [650,360,640,350,630,360,640,370,650,360]),
            ('c3B', (255,0,0)*5))
        t = time.time() - self.starttime
        for fplotter in self.fplotters:
            vlist = []
            zlist = fplotter.hands_vertexlist(t)
            n = len(zlist)
            while zlist:
                z = zlist.pop(0)
                vlist.append(z.real*self.scale+self.xoffset)
                vlist.append(z.imag*self.scale+self.yoffset)
            self.phasordict[fplotter] = self.batch.add(n, 
                pyglet.gl.GL_LINE_STRIP, None,
                ('v2f', vlist),
                ('c3B', (0,255,0)*n) )
            tlist = []
            tlen = len(fplotter.trace)
            for z in fplotter.trace:
                tlist += [z.real*self.scale+self.xoffset,
                    z.imag*self.scale+self.yoffset]
            self.tracedict[fplotter] = self.batch.add(n, 
                pyglet.gl.GL_LINE_STRIP, None,
                ('v2f', vlist),
                ('c3B', (0,255,0)*n) )


    def update(self, dt):
        t = time.time() - self.starttime
        for fplotter in self.fplotters:
            zlist = fplotter.hands_vertexlist(t)
            n = len(zlist)
            for k in range(n):
                z = zlist[k]
                self.phasordict[fplotter].vertices[2*k:2*(k+1)] = (
                    z.real*self.scale+self.xoffset,
                    z.imag*self.scale+self.yoffset)
            tlist = []
            tlen = len(fplotter.trace)




        

    def scalez(self, z):
        return z.real*self.scale+self.xoffset, z.imag*self.scale+self.yoffset

    def run(self):
        self.init_graphics()
        print(self.phasordict)

        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()


class FourierGraph:
    # To plot the graph of the real part
    # To be implemented
    pass
    def __init__(self):
        no_points = 200
        self.fplotters = []
    
    def add_fplotter(self, fplotter):
        self.fplotters.append(fplotter)

    def curves(self):
        dt = 1/self.no_points
        curvelist = []
        for fplotter in self.fplotters:
            termlist = self.termlist(t)
            t = 0
            ylist = []
            for k in range(no_plots):
                tlist = fplotter.termlist(t)
                z = sum(tlist)
                y = z.real
                ylist.append(y)
            curvelist.append(ylist)
        return curvelist

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
#print(plist)

'''
fa.batch.add(len(points), 
            pyglet.gl.GL_LINE_STRIP,
            None, 
            ('v2f', plist),
            ('c3B', (0,255,0)*len(points)))

fa.batch.add(2, 
            pyglet.gl.GL_LINE_STRIP,
            None, 
            ('v2f', [0,0,300,300]),
            ('c3B', (0,255,255,0,255,255)))
'''
fa.set_axes(200,640,360)
fa.add_fplotter(fp)
fa.add_fplotter(fp2)
print(fa.starttime,fa.fplotters,fa.batch)
fa.run()
