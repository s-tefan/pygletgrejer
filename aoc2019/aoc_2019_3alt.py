# Advent of Code 2019
# Day 3, Part 1

import sys

class Wiresection:
    # Has a direction in {'U','D','L','R','O'} and a length
    # If length if 0, direction is 'O'
    __init__(self,dir='O',length=0,start=None

    @staticmethod
    def determine_intersect(min,max,const):
        return min<=const and const<=max


    def intersects(self,osec):
        if self.direction == 'U':
            if osec.direction == 'L':
                return determine_intersect(self.start[1], self.start[1]+self.length, osec.start[1]) and
                        determine_intersect(osec.start[0], osec.start[0]+self.length, self.start[0])
            elif osec.direction == 'R':
                return determine_intersect(self.start[1], self.start[1]+self.length, osec.start[1]) and
                        determine_intersect(osec.start[0]-self.length, osec.start[0], self.start[0])
        # osv...



        
def fixinput(line):
    # decodes a line of move operators to a list
    # of tuples (direction,steps) where direction
    # is a character and steps an integer
    sections=[]
    sec_string_list = line.strip().split(',')
    for sec_str in sec_string_list:
        direction = sec_str[0]
        steps =  int(sec_str[1:])
        sections.append(Wiresection(direction,steps))
    return sections

def getinput(file):
    wires=[]
    for line in file:
        moves = fixinput(line)
        wires.append(moves)
    return wires

def movesort(wire):
    pos=[0,0]
    for move in wire
    if move[0] in 'U':
        sectio
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





def manhattan(pos):
    return abs(pos[0])+abs(pos[1])

wires=getinput(sys.stdin)
xings=findcrossingset(wires)
#print(xings)
xingsdist=set(map(manhattan,xings))
#print(xingsdist)
print(min(xingsdist))

print(findcrossingdict_minsteps(wires))


        


