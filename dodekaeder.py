import math
import pyglet
import pyglet.graphics as pg
import pyglet.gl as pgl
class Dodekaeder:
    def __init__(self):
        phi = (1+math.sqrt(5))/2 
        iphi = 1/phi
        self.vertices = (
            (-iphi,0,-phi), (iphi,0,-phi), #blå 0-1
            (-1,-1,-1), (-1,1,-1),(1,1,-1),(1,-1,-1), #orange 2-5
            (0,-phi,-iphi), (0,phi,-iphi), #grön 6-7
            (-phi,-iphi,0),(-phi,iphi,0),(phi,iphi,0),(phi,-iphi,0), #röd 8-11
            (0,-phi,iphi), (0,phi,iphi), #grön 12-13
            (-1,-1,1), (-1,1,1),(1,1,1),(1,-1,1), #orange 14-17
            (-iphi,0,phi), (iphi,0,phi) #blå 18-19
        )
        self.edges = (
            (0,1), 
            (0,2), (0,3), (1,4), (1,5), #blå-orange
            (2,6), (5,6), (3,7), (4,7), #orange-grön
            (2,8), (3,9), (4,10), (5,11), #orange-röd
            (6,12), (7,13), (8,9), (10,11), #grön-grön, röd-röd
            (8,14), (9,15), (10,16), (11,17), #röd-orange
            (12,14), (12,17), (13,15), (13,16), #grön-orange
            (14,18), (15,18), (16,19), (17,19), #orange-blå
            (18,19)
        )
        self.faces = (
            (0,1,5,6,2),
            (1,0,3,7,4),
            (0,2,8,9,3),
            (1,4,10,11,5), # osv
            (18,19,16,13,15), (19,18,14,12,17) # sista
        )
        self.batch = pg.Batch()
        
        # vertices
        self.vert_list = self.batch.add(20, pgl.GL_POINTS, None, 
            ('v3f',
            [coord for vertex in self.vertices for coord in vertex]
            )
        )
        # edges
        vlist = []
        for e in self.edges:
            vlist += self.vertices[e[0]]
            vlist += self.vertices[e[1]]
        self.edge_list = self.batch.add(len(vlist)//3, pgl.GL_LINES, None,
            ('v3f', vlist.copy())
        )
        
        # faces
        self.face_list = []
        clist = [(1,0,0,0.1), (0,1,0,0.1), 
            (0,0,1,0.1), (0,0,1,0.1), 
            (1,0,0,0.1),(0,1,0,0.1)]
        for f in self.faces:
            vlist = []
            for ind in f:
                vlist += self.vertices[ind]
            #vlist += self.vertices[f[0]]
            self.face_list.append(self.batch.add(5, pgl.GL_POLYGON, None, 
                ('v3f', vlist.copy()),
                ('c4f', clist.pop(0)*5)
            ))
        # Polygonerna blir inte som de ska nu med Batch...

''' De här behövs inte med Batch
    def gl_vertices(self):
        return pg.vertex_list(20, ('v3f',
            [coord for vertex in self.vertices for coord in vertex])
        )

    def gl_edges(self):
        vlist = []
        for e in self.edges:
            vlist += self.vertices[e[0]]
            vlist += self.vertices[e[1]]
        return pg.vertex_list(len(vlist)//3,
            ('v3f', vlist)
        )
        
    def gl_faces(self):
        flist = []
        clist = [(1,0,0,0.1), (0,1,0,0.1), 
            (0,0,1,0.1), (0,0,1,0.1), 
            (1,0,0,0.1),(0,1,0,0.1)]
        for f in self.faces:
            vlist = []
            for ind in f:
                vlist += self.vertices[ind]
            flist.append(pg.vertex_list(5, 
                ('v3f', vlist),
                ('c4f', clist.pop(0)*5)))
        return flist
'''

win = pyglet.window.Window()

apa = Dodekaeder()
'''glv = apa.gl_vertices()
gle = apa.gl_edges()
glflist = apa.gl_faces()
grp = pg.Group()
b = pg.Batch()
b.add(gle.count, pgl.GL_LINES, None, ('v3f',gle.vertices) )
b.add(glv.count, pgl.GL_POINTS, None, ('v3f',glv.vertices) )
for glf in glflist:
    b.add(glf.count, pgl.GL_POLYGON, None, 
        ('v3f',glf.vertices), ('c4f',(1,0,0,0.1)*glf.count))
'''

@win.event
def on_draw():
    win.clear()
    '''
    for glf in glflist:
        glf.draw(pgl.GL_POLYGON)
    glv.draw(pgl.GL_POINTS)
    gle.draw(pgl.GL_LINES)
    '''
    apa.batch.draw()
@win.event
def on_resize(width,height):
    pgl.glBlendFunc(pgl.GL_SRC_ALPHA, pgl.GL_ONE_MINUS_SRC_ALPHA)
    pgl.glViewport(0, 0, 400, 400)
    #pgl.glEnable(pgl.GL_CULL_FACE)
    pgl.glScalef(100,100,0.01)
    pgl.glTranslatef(2,2,2)
    pgl.glRotatef(10,0,0,1)

def update(dt):
    #pgl.glRotatef(1,1/3**(1/2),1/3**(1/2),1/3**(1/2))
    pgl.glRotatef(1,1,1,1)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()