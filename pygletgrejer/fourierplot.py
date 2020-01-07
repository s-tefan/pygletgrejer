import pyglet
import cmath
import time
import numpy.fft
import random

'''
Borde byggas om objektorienterat med en klass Fourierplotter eller liknande.
De globala variablerna är då attribut till ett objekt.
'''


# global variables
g_tick = 0
twopii = 2j*cmath.pi
scale = 200
xoffset = 640
yoffset = 360
omega = 1/20
nt = 100
tracelist = [0]*(2*nt)


plist = [1,1+0.25j,1+0.5j,1+0.75j, 
    1+1j,0.75+1j,0.5+1j,0.25+1j,0+1j,-0.25+1j,-0.5+1j,-0.75+1j,
    -1+1j,-1+0.75j,-1+0.5j,-1+0.25j,-1+0j,-1-0.25j,-1-0.5j,-1-0.75j,
    -1-1j,-0.75-1j,-0.5-1j,-0.25-1j,0-1j,0.25-1j,0.5-1j,0.75-1j,
    1-1j,1-0.75j,1-0.5j,1-0.25j] # 32 element från en kvadrat


plist = [cmath.exp(twopii*k/16)+(random.uniform(-1,1)+1j*random.uniform(-1,1)) for k in range(16)]
#flist = numpy.fft.fft(plist,norm = "ortho")

#plist = plist[::4]
#plist = [0,0.5,1,0.5+0.5j,1j,0.5j]
#plist = [0,0.5,1,1j,0.5j]
flist = [c/len(plist) for c in numpy.fft.fft(plist)]
n = len(flist)//2

def poscoeff(n):
    return flist[n]
def negcoeff(n):
    return flist[-n]
def constcoeff():
    return flist[0]




def blaha(t,n):
    global tracelist
    z = constcoeff()
    x = xoffset+scale*z.real
    y = yoffset+scale*z.imag
    vlist = [x,y]
    for k in range(1,(n+1)//2):
        z += poscoeff(k)*cmath.exp(twopii*k*t)
        vlist.append(xoffset+scale*z.real)
        vlist.append(yoffset+scale*z.imag)
        z += negcoeff(k)*cmath.exp(-twopii*k*t)
        vlist.append(xoffset+scale*z.real)
        vlist.append(yoffset+scale*z.imag)
    if n%2 == 0:
        z += poscoeff(n//2)*cmath.exp(twopii*t*(-n//2))
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


def blaha2(t,n):
    z = constcoeff()
    x = xoffset+scale*z.real
    y = yoffset+scale*z.imag
    vlist = [x,y]
    for k in range(1,n):
        if k > n//2:
            m = k-n
        else:
            m = k
        z += poscoeff(k)*cmath.exp(twopii*m*t)
        vlist.append(xoffset+scale*z.real)
        vlist.append(yoffset+scale*z.imag)
    x = xoffset+scale*z.real
    y = yoffset+scale*z.imag
    vlistq =  [x+2, y+2, x+2, y-2, x-2, y-2, x-2, y+2]
    return vlist, vlistq

def blaha3(t,n):
    vlist = []
    z = 0
    ind = list(range(n))
    if n%2 == 0:
        ind[1] = n//2
        for k in range(1,n//2):
            ind[n//2+1-k] = k
            ind[n//2+k] = -k 
    else:
        for k in range(1,(n+1)//2):
            ind[n//2-k+1] = k
            ind[n//2+k] = -k
    for k in ind:
        z += poscoeff(k)*cmath.exp(twopii*k*t)
        vlist.append(xoffset+scale*z.real)
        vlist.append(yoffset+scale*z.imag)
    x = xoffset+scale*z.real
    y = yoffset+scale*z.imag
    vlistq =  [x+2, y+2, x+2, y-2, x-2, y-2, x-2, y+2]
    return vlist, vlistq

def update(dt):
    global vertex_list, vertex_list2, vertex_list3, quad, quad2, trace, tracelist, starttime, p
    t = time.time()-starttime
    vlists = blaha(omega*t,len(flist))
    vlists2 = blaha2(omega*t,len(flist))
    vlists3 = blaha3(omega*t,len(flist))
    vertex_list = pyglet.graphics.vertex_list(len(vlists[0])//2, \
        ('v2f', vlists[0] ))
    vertex_list2 = pyglet.graphics.vertex_list(len(vlists2[0])//2, \
        ('v2f', vlists2[0] ))
    vertex_list3 = pyglet.graphics.vertex_list(len(vlists3[0])//2, \
        ('v2f', vlists3[0] ))
    quad = pyglet.graphics.vertex_list(4, \
        ('v2f', vlists[1]),('c3B', (255,0,0)*4))
    quad2 = pyglet.graphics.vertex_list(4, \
        ('v2f', vlists2[1]),('c3B', (0,255,0)*4))
    trace = pyglet.graphics.vertex_list(len(tracelist)//2, \
        ('v2f', tracelist),('c3B', (255,0,0)*nt))

starttime = time.time()
pyglet.clock.schedule_interval(update, 1/30)
win = pyglet.window.Window(1280,720)
pvlist = []
for z in plist:
    pvlist += [xoffset+scale*z.real,yoffset+scale*z.imag]
p = pyglet.graphics.vertex_list(len(plist), \
    ('v2f', pvlist),('c3B', (0,255,255)*len(plist)))
update(0)




@win.event
def on_draw():
    global vertex_list, vertex_list2, vertex_list3, quad, quad2, trace, p
    win.clear()
    vertex_list.draw(pyglet.gl.GL_LINE_STRIP)
    vertex_list2.draw(pyglet.gl.GL_LINE_STRIP)
    vertex_list3.draw(pyglet.gl.GL_LINE_STRIP)
    quad.draw(pyglet.gl.GL_QUADS)
    quad2.draw(pyglet.gl.GL_QUADS)
    trace.draw(pyglet.gl.GL_LINE_STRIP)
    p.draw(pyglet.gl.GL_POINTS)



pyglet.app.run()

