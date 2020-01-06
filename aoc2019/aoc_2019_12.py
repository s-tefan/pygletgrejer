def lcd(a,b):
    if a%b == 0:
        return b
    else:
        return lcd(b,a%b)

def gcm(nlist):
    a = nlist[0]
    for k in range(1,len(nlist)):
        a = a*nlist[k]//lcd(a,nlist[k])
    return a

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

    def cycle_coord(self, coordn):
        start_positions = [ sat.position[coordn] for sat in self.satellites ]
        start_velocities = [ sat.velocity[coordn] for sat in self.satellites ]
        positions = start_positions.copy()
        velocities = start_velocities.copy()
        repeat = True
        n = len(positions)
        k = 0
        while repeat:
            for p in range(n):
                g = 0
                for q in range(n):
                    if q != p:
                        g += ((positions[q]>positions[p])-(positions[q]<positions[p]))
                velocities[p] += g
            for p in range(n):
                positions[p] += velocities[p]
            k += 1
            repeat = (positions != start_positions or velocities != start_velocities)
        return k






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

def part1():
    io = Satellite([0,6,1])
    europa = Satellite([4,4,19])
    ganymede = Satellite([-11,1,8])
    callisto = Satellite([2,19,15])
    jupiter_moons = System([io, europa, ganymede, callisto])

    for _ in range(1000):
        jupiter_moons.update()
        for moon in jupiter_moons.satellites:
            print(moon.position,moon.velocity)
        #print(jupiter_moons.total_energy())
        #input()
        return jupiter_moons.total_energy()

def part2():
    io = Satellite([0,6,1])
    europa = Satellite([4,4,19])
    ganymede = Satellite([-11,1,8])
    callisto = Satellite([2,19,15])
    jupiter_moons = System([io, europa, ganymede, callisto])
    cycles = [ jupiter_moons.cycle_coord(k) for k in range(3) ]
    return(gcm(cycles))

import time
t0 = time.process_time()
p1=part1()
t1 = time.process_time()
print('Part 1:',p1,'process time', t1-t0,'seconds')
t2 = time.process_time()
p2=part2()
t3 = time.process_time()
print('Part 2:',p2,'process time', t3-t2,'seconds')
