import sys


def fixinput(line):
    moves=[]
    strippedline = line.strip().split(',')
    for movestr in strippedline:
        direction = movestr[0]
        steps =  int(movestr[1:])
        moves.append((direction,steps))
    return moves

def getinput(file):
    wires=[]
    for line in file:
        moves = fixinput(line)
        wires.append(moves)
    return wires

def movepos(pos,move):
    # den här ska vi inte använda ...
    if move[0]=='U':
        pos[1]+=move[1]
    elif move[0]=='D':
        pos[1]-=move[1]
    elif move[0]=='R':
        pos[0]+=move[1]
    elif move[0]=='L':
        pos[0]-=move[1]
    else:
        raise ValueError('Forbidden direction')

def moveposstep(pos,dir):
    if dir=='U':
        pos[1]+=1
    elif dir[0]=='D':
        pos[1]-=1
    elif dir=='R':
        pos[0]+=1
    elif dir=='L':
        pos[0]-=1
    else:
        raise ValueError('Forbidden direction')


def getwirepoints(wire):
    # as list of tuples
    pos=[0,0]
    wirepoints=[tuple(pos)]
    for move in wire:
        for k in range(move[1]):
            moveposstep(pos,move[0])
            wirepoints.append(tuple(pos))
    return wirepoints

def getwirepointset(wire):
    # as set of tuples
    pos=[0,0]
    wirepointset=set()
    for move in wire:
        for k in range(move[1]):
            moveposstep(pos,move[0])
            wirepointset.add(tuple(pos))
    return wirepointset



def findcrossingset(wires):
    wirepointset0=getwirepointset(wires[0])
    wirepointset1=getwirepointset(wires[1])
    return wirepointset0 & wirepointset1

def manhattan(pos):
    return abs(pos[0])+abs(pos[1])

wires=getinput(sys.stdin)
xings=findcrossingset(wires)
#print(xings)
xingsdist=set(map(manhattan,xings))
#print(xingsdist)
print(min(xingsdist))

        


