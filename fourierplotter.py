import cmath
import numpy.fft
import time

pi2i = 2*cmath.pi*1j

class Fourierplotter:
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

    def __init__(self, width = 1280, heigth = 720):
        self.starttime = time.time()
        win = pyglet.window.Window(width,height)

    def add_fplotter(self, fplotter, scale = 1, xoffset = 0, yoffset = 0):
        pass




