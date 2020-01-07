import pyglet
from pyglet.window import mouse
import math

# global variables
g_tick = 0


def pointcoords_to_vertex_list(points, color, offset=(0,0), scale=(1,1)):
    # point is a sequence of 2d coordinates, as number pairs
    # color is a rgb-triple of integers (unsigned bytes)
    # returns a vertex list 
    vlist = []
    n = len(points)
    for point in points:
        vlist.append(offset[0]+scale[0]*point[0])
        vlist.append(offset[1]+scale[1]*point[1])
    clist = color*n

    return (pyglet.graphics.vertex_list(n, \
        ('v2f', vlist), ('c3B',clist) ))




sinlist = []
for k in range(51):
    x = 2*math.pi*k/50
    y = math.sin(x)
    sinlist.append((x,y))

t = [0,1,2,3,4,5,8,10,17,24,61,71,78,110]
temp = [85.4, 80.1, 77.8, 74.9, 73.1, 69.9, \
    65.0, 61.0, 52.6, 47.2, 32.1, 30.1, 28.9, 25.4]
reltemp = [te-22.4 for te in temp]
rtl = [math.log(te)for te in reltemp]
pointlist = list(zip(t,reltemp))
pointlist2 = list(zip(t,rtl))

# Hela
rtl_x = t
rtl_y = rtl
rtl_x2 = [x*x for x in rtl_x]
rtl_xy = [x*y for (x,y) in zip(rtl_x, rtl_y)] 
n = len(rtl_x)
det = n*sum(rtl_x2)-sum(rtl_x)**2
m = (sum(rtl_x2)*sum(rtl_y)-sum(rtl_x)*sum(rtl_xy))/det
k = (n*sum(rtl_xy)-sum(rtl_x)*sum(rtl_y))/det
pointlist3 = [(rtl_x[0],rtl_x[0]*k+m),(rtl_x[-1],rtl_x[-1]*k+m)]
print(k, m)

# Utan första fyra
rtl_x = t[4:]
rtl_y = rtl[4:]
rtl_x2 = [x*x for x in rtl_x]
rtl_xy = [x*y for (x,y) in zip(rtl_x, rtl_y)] 
n = len(rtl_x)
det = n*sum(rtl_x2)-sum(rtl_x)**2
m = (sum(rtl_x2)*sum(rtl_y)-sum(rtl_x)*sum(rtl_xy))/det
k = (n*sum(rtl_xy)-sum(rtl_x)*sum(rtl_y))/det
pointlist4 = [(rtl_x[0],rtl_x[0]*k+m),(rtl_x[-1],rtl_x[-1]*k+m)]
print(k, m)

win = pyglet.window.Window()
my_vlist = pointcoords_to_vertex_list(pointlist, \
    (255,0,0), (10,0), (5,5))
my_vlist2 = pointcoords_to_vertex_list(pointlist2, \
    (0,0,255), (10,-100), (5,100))
my_vlist3 = pointcoords_to_vertex_list(pointlist3, \
    (0,255,0), (10,-100), (5,100))
my_vlist4 = pointcoords_to_vertex_list(pointlist4, \
    (255,255,0), (10,-100), (5,100))



@win.event
def on_draw():
    win.clear()
    my_vlist.draw(pyglet.gl.GL_LINE_STRIP)
    my_vlist2.draw(pyglet.gl.GL_LINE_STRIP)
    my_vlist3.draw(pyglet.gl.GL_LINE_STRIP)
    my_vlist4.draw(pyglet.gl.GL_LINE_STRIP)

pyglet.app.run()

