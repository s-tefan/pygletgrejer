import math
import numpy as np
import pyglet
from pyglet.gl import *

win = pyglet.window.Window()

# get all the points in a circle centered at 0.
def PointsInCircum(r, n=360, pi=math.pi):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]
pts = np.array(PointsInCircum(1))

# function that increments to the next
# point along a circle
frame = 0
def update_frame(dt):
    global frame
    if frame == None or frame == pts.shape[0]-1:
        frame = 0
    else:
        frame += 1
    print(frame)

@win.event
def on_draw():
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT)
    # draw the next line
    # in the circle animation


    glBegin(GL_LINES)
    glVertex3f(1,1,0)
    glVertex3f(pts[frame][1],pts[frame][0],0)
    glVertex3f(1,1,0)
    glEnd()
    glBegin(GL_POLYGON)
    n = len(pts)
    glVertex3f(pts[frame][1],pts[frame][0],0)
    glColor3ub(0,0,255)
    glVertex3f(pts[(frame+n//4)%n][1],pts[(frame+n//4)%n][0],0)
    glColor3ub(0,255,0)
    glVertex3f(pts[(frame+n//2)%n][1],pts[(frame+n//2)%n][0],0)
    glColor3ub(255,0,0)
    glVertex3f(pts[(frame-n//4)%n][1],pts[(frame-n//4)%n][0],0)
    glEnd()



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




# every 1/10 th get the next frame
pyglet.clock.schedule_interval(update_frame, 1/10)
pyglet.app.run()
