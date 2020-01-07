import cmath
import numpy.fft

pi2i = 2*cmath.pi*1j

class Fourierplotter:
    def __init__(self, flist=[])
        self.flist = flist
    
    def termlist(self.t):
        n = len(flist)
        return [exp(pi2i*k/n)*self.flist[k] for k in range(n)]
    
    def setpoints(self.plist):
        flistraw = numpy.fft.fft(plist)
        n = len(flistraw)
        self.flist = [f/n for f in flistraw]
    
    def hands_vertexlist(self, t, scale = 1, xoffset = 0, yoffset = 0):
        tlist = self.termlist(t)
        z = tlist[0]
        zlist = [z]
        n = len(tlist)
        for k in range(1,n//2): #?
            z += tlist[k]
            zlist.append(z)
            z += tlist[n-k]
            zlist.append(z)
        if n%2:
            z += tlist[n//2]
            zlist.append(z)
        return zlist


