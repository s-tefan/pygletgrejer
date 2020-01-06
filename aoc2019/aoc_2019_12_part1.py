class Satellite:
    def __init__(self, pos):
        self.position = list(pos)
        self.velocity = [0,0,0]
    
    def pot_en(self):
        return sum(abs(x) for x in self.position)
    
    def kin_en(self):
        return sum(abs(x) for x in self.velocity)


class System:
    def __init__(self, satellites):
        self.satellites = satellites
    
    def update_velocity(self):
        for p in self.satellites:
            for q in self.satellites:
                if p != q:
                    p.velocity = list(iter_sum(p.velocity,iter_cmp(q.position,p.position)))

    def update_position(self):
        for p in self.satellites:
            for k in range(len(p.position)):
                p.position[k] += p.velocity[k]

    def update(self):
        self.update_velocity()
        self.update_position()

    def total_energy(self):
        return sum(p.pot_en() * p.kin_en() for p in self.satellites) # sic: *, not +




def cmp(a,b):
    return (a>b)-(a<b)

def iter_cmp(a,b):
    return (cmp(*p) for p in zip(a,b))
    # returns a generator object
    # needs to be converted to the type you want
    # note that the generator is emptied in conversion
def iter_sum(a,b):
    return (sum(p) for p in zip(a,b))
    # returns a generator object
    # needs to be converted to the type you want
    # note that the generator is emptied in conversion



'''
<x=0, y=6, z=1>
<x=4, y=4, z=19>
<x=-11, y=1, z=8>
<x=2, y=19, z=15>
'''

io = Satellite([0,6,1])
europa = Satellite([4,4,19])
ganymede = Satellite([-11,1,8])
callisto = Satellite([2,19,15])
jupiter_moons = System([io, europa, ganymede, callisto])


for k in range(1000):
    jupiter_moons.update()
    for moon in jupiter_moons.satellites:
        print(moon.position,moon.velocity)
    print(jupiter_moons.total_energy())
    input()
'''
for moon in jupiter_moons.satellites:
    print(moon.position,moon.velocity)
print(jupiter_moons.total_energy())
'''
print(jupiter_moons.total_energy())

io = Satellite([0,6,1])
europa = Satellite([4,4,19])
ganymede = Satellite([-11,1,8])
callisto = Satellite([2,19,15])
jupiter_moons = System([io, europa, ganymede, callisto])

repeat = True
k = 0

while repeat:
    k+=1
    # check if returned

