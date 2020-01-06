# Advent of Code 2019
# Day 3, Part 1

import sys


def fixinput(line):
    # decodes a line of move operators to a list
    # of tuples (direction,steps) where direction
    # is a character and steps an integer
    moves=[]
    movestringlist = line.strip().split(',')
    for movestr in movestringlist:
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
    # not used
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

def getwirepointlengthdict(wire):
    # as set of tuples
    pos=[0,0]
    wirepointdict={}
    steps=0
    for move in wire:
        for k in range(move[1]):
            steps+=1
            moveposstep(pos,move[0])
            wirepointdict[tuple(pos)]=steps
    return wirepointdict


def findcrossingset(wires):
    wirepointset0=getwirepointset(wires[0])
    wirepointset1=getwirepointset(wires[1])
    return wirepointset0 & wirepointset1

def findcrossingdict_minsteps(wires):
    wirepointdict0 = getwirepointlengthdict(wires[0])
    wirepointdict1 = getwirepointlengthdict(wires[1])
    intersect = set(wirepointdict0) & set(wirepointdict1)
    stepslist=[]
    for crossing in intersect:
        steps = wirepointdict0[crossing]+wirepointdict1[crossing]
        stepslist.append(steps)
    return min(stepslist)




def manhattan(pos):
    return abs(pos[0])+abs(pos[1])

wires=getinput(sys.stdin)
xings=findcrossingset(wires)
#print(xings)
xingsdist=set(map(manhattan,xings))
#print(xingsdist)
print(min(xingsdist))

print(findcrossingdict_minsteps(wires))


        


