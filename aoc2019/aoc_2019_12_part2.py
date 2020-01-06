
def count(start_positions):
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

def lcd(a,b):
    if a%b == 0:
        return b
    else:
        return lcd(b,a%b)


import time
t0 = time.process_time()
start_velocities = [0,0,0,0] #global
xc = count([0,4,-11,2])
print(xc)
yc = count([6,4,1,19])
print(yc)
zc = count([1,19,8,15])
print(zc)
mcd1 = xc*yc//lcd(xc,yc)
mcd = mcd1*zc//lcd(mcd1,zc)
print(mcd)
t1 = time.process_time()
print('process time', t1-t0,'seconds')
'''
<x=0, y=6, z=1>
<x=4, y=4, z=19>
<x=-11, y=1, z=8>
<x=2, y=19, z=15>
'''

