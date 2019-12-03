import graphics as g

class Mandel:
    max=100


    def __init__(self,c1,c2):
        self.c1,self.c2=c1,c2
        #print(c1,c2)
        self.num=self.count(self.max)
        self.east=None
        self.north=None
        self.northeast=None
        self.isleaf=True


    def count(self,n):
        z=self.c1
        for k in range(n):
            z=z**2+self.c1
            if abs(z)>2:
                return k
        return n
    
    def quart(self):
        diff=(self.c2-self.c1)/2
        self.east=Mandel(self.c1+diff.real,self.c1+diff.real+diff)
        self.north=Mandel(self.c1+diff.imag,self.c1+diff.imag+diff)
        self.northeast=Mandel(self.c1+diff,self.c1+2*diff)
        self.isleaf=False

    def refine(self):
        if self.isleaf:
            self.quart()
        else:
            self.east.refine()
            self.north.refine()
            self.northeast.refine()


    def print(self):
        if self.isleaf:
            print(self.c1,self.c2,self.num)
        else:
            self.east.print()
            self.north.print()
            self.northeast.print()

    def image(self,width):
        diff=self.c2-self.c1
        step=diff.real/width
        height=int(diff.imag/step)
        #...
        




#win=g.GraphWin(width=1000,height=1000)

m=Mandel(-.1-.1j,.1+.1j)
for k in range(10):
    m.print()
    print('-')
    m.refine()
