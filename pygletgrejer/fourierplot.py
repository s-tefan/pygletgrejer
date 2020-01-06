import pyglet
from pyglet.window import mouse
import cmath
import time
import numpy.fft
import random

'''
Borde byggas om objektorienterat med en klass Fourierplotter eller liknande
De globala variablerna är då attribut till ett objekt
'''


# global variables
g_tick = 0
twopii = 2j*cmath.pi
scale = 200
xoffset = 640
yoffset = 360
omega = 1/10
nt = 100
tracelist = [0]*(2*nt)

'''
plist = [1,1+0.25j,1+0.5j,1+0.75j, 
    1+1j,0.75+1j,0.5+1j,0.25+1j,0+1j,-0.25+1j,-0.5+1j,-0.75+1j,
    -1+1j,-1+0.75j,-1+0.5j,-1+0.25j,-1+0j,-1-0.25j,-1-0.5j,-1-0.75j,
    -1-1j,-0.75-1j,-0.5-1j,-0.25-1j,0-1j,0.25-1j,0.5-1j,0.75-1j,
    1-1j,1-0.75j,1-0.5j,1-0.25j] # 32 element från en kvadrat
'''
plist = [cmath.exp(twopii*k/16)+(random.uniform(-0.25,0.25)+1j*random.uniform(-0.25,0.25)) for k in range(16)]
#flist = numpy.fft.fft(plist,norm = "ortho")
flist = [c/len(plist) for c in numpy.fft.fft(plist)]
n = len(flist)//2


def poscoeff(n):
    #return 1j/n + 1/n*cmath.exp(twopii*n/4)
    return flist[n]
def negcoeff(n):
    #return -1j/n - 1/n*cmath.exp(twopii*n/4)
    return flist[-n]
def constcoeff():
    #return cmath.pi/2
    return flist[0]




def blaha(t,n):
    global tracelist
    z = constcoeff()
    x = xoffset+scale*z.real
    y = yoffset+scale*z.imag
    vlist = [x,y]
    for k in range(1,n+1):
        z += poscoeff(k)*cmath.exp(twopii*k*t)
        vlist.append(xoffset+scale*z.real)
        vlist.append(yoffset+scale*z.imag)
        z += negcoeff(k)*cmath.exp(-twopii*k*t)
        vlist.append(xoffset+scale*z.real)
        vlist.append(yoffset+scale*z.imag)
    x = xoffset+scale*z.real
    y = yoffset+scale*z.imag
    vlistq =  [x+2, y+2, x+2, y-2, x-2, y-2, x-2, y+2]
    tracelist.pop(0)
    tracelist.pop(0)
    tracelist.append(x)
    tracelist.append(y)
    return vlist, vlistq

def update(dt):
    global vertex_list, quad, trace, tracelist, starttime
    t = time.time()-starttime
    vlists = blaha(omega*t,n)
    vertex_list = pyglet.graphics.vertex_list(2*n+1, \
        ('v2f', vlists[0] ))
    quad = pyglet.graphics.vertex_list(4, \
        ('v2f', vlists[1]),('c3B', (255,0,0)*4))
    trace = pyglet.graphics.vertex_list(nt, \
        ('v2f', tracelist),('c3B', (255,0,0)*nt))

starttime = time.time()
pyglet.clock.schedule_interval(update, 1/30)
win = pyglet.window.Window(1280,720)
vlists = blaha(0,n)
pvlist = []
for z in plist:
    pvlist += [xoffset+scale*z.real,yoffset+scale*z.imag]
vertex_list = pyglet.graphics.vertex_list(2*n+1, \
    ('v2f', vlists[0] ))
quad = pyglet.graphics.vertex_list(4, \
    ('v2f', vlists[1]),('c3B', (255,0,0)*4)  )
trace = pyglet.graphics.vertex_list(nt, \
    ('v2f', tracelist),('c3B', (255,0,0)*nt))
p = pyglet.graphics.vertex_list(len(plist), \
    ('v2f', pvlist),('c3B', (0,255,255)*len(plist)))


@win.event
def on_draw():
    global vertex_list, quad, trace, p
    win.clear()
    vertex_list.draw(pyglet.gl.GL_LINE_STRIP)
    quad.draw(pyglet.gl.GL_QUADS)
    trace.draw(pyglet.gl.GL_LINE_STRIP)
    p.draw(pyglet.gl.GL_POINTS)



pyglet.app.run()

