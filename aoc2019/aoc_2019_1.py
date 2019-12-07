# adventofcode2019 #1

import sys

def fuelreq(masses):
    return sum(map(lambda x: x//3-2, masses))

def fueliterate(mass):
    fuelsum=0
    fuel=mass//3-2
    while fuel>0:
        fuelsum+=fuel
        fuel=fuel//3-2
    return fuelsum

def fuelreq2(masses):
    return sum(map(fueliterate, masses))


mymasses=[]
for line in sys.stdin:
    try:
        mymasses.append(int(line.strip()))
    except:
        pass    

print(fuelreq2(mymasses))

