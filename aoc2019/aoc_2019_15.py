import aoc_2019_intcode as ic

'''
Strategy: Try different directions in a breadth first traversion until oxygen system found
Saving a copy of the intcode program for each direction recursively
Part one: stop when oxygen is found
Part two: note at which level there are no branches left.
'''

#globals
g_levellist = [[]]
verbose = False

def save_state(level, state):
    # saves the state at a point in the walk
    global g_levellist
    g_levellist[level].append(state)

def try_dir(dir, code):
    # try a direction
    status = code.run_io([dir])
    #print(status)
    return status[0]


def try_dirs(level, state):
    # try every direction except going back
    # check for oxygen system
    # save the state for every path forward
    back = (0,2,1,4,3)[state['lastdir']]
    for dir in range(1,5):
        if dir != back:
            newstate = state.copy()
            newstate['code'] = state['code'].copy()
            t = try_dir(dir,newstate['code'])
            newstate['status'] = t
            if t == 2:
                if verbose: print("OXYGEN!")
                newstate['lastdir'] = dir
                newpath = state['path'].copy()
                newpath.append(dir)
                newstate['path'] = newpath
                save_state(level, newstate)
                return 'oxygen'
            elif t == 1:
                newstate['lastdir'] = dir
                newpath = state['path'].copy()
                newpath.append(dir)
                newstate['path'] = newpath
                save_state(level, newstate)
                pass
    #print(g_levellist)
    return 'ok'

def traverse_level(level):
    # traverse a level
    g_levellist.append([])
    for muck in g_levellist[level]:
        status = try_dirs(level+1, muck)
        if status == 'oxygen':
            return 'oxygen'
    return 'ok'


def part1(intcode):
    # solve part one by traversing breadth first
    running = True
    level = 0
    g_levellist[0] = [{'lastdir':0, 'code':intcode.copy(), 'path':[]}]
    while running:
        if verbose: print('Traversing level {}!'.format(level))
        status = traverse_level(level)
        level +=1
        if status == 'oxygen':
            if verbose: print('Oxygen found after {} steps'.format(level))
            return level
        #print_cave(g_levellist)
        if not g_levellist[level]: break # break if all paths ended.

            
def part2():
    # solve part two by traversing breadth first from the oxygen system
    # until there are no more paths forward
    global g_levellist
    state = g_levellist[-1][-1]
    newstate = state.copy()
    newstate['code'] = state['code'].copy()
    newstate['lastdir'] = 0
    newpath = []
    newstate['path'] = newpath
    running = True
    level = 0
    g_levellist = [[]]
    g_levellist[0] = [newstate]
    while running:
        if verbose: print('Traversing level {}!'.format(level))
        traverse_level(level)
        if g_levellist[level]:
            level += 1
        else:
            break
    if verbose: print("It takes {} minutes to fill the area with oxygen".format(level-1))
    return level-1



def print_cave(level_list):
    pset = set()
    for level in level_list:
        for k in level:
            pos = [0,0]
            for move in k['path']:
                d = [(0,0),(0,-1),(0,1),(-1,0),(1,0)][move]
                pos[0] += d[0]
                pos[1] += d[1]
            pset.add(tuple(pos))
    we,ns = list(zip(*pset))
    wemin, wemax, nsmin, nsmax = min(we), max(we), min(ns), max(ns)
    canvas = []
    for k in range(nsmax-nsmin+3):
        canvas.append(['#']*(wemax-wemin+3))
    for pos in pset:
        canvas[pos[1]-nsmin+1][pos[0]-wemin+1]=' '
    for row in canvas:
        print(''.join(row))


import time

def day15():
    with open("input15.txt","r") as f:
        intcode = ic.IntcodeIO()
        s = f.read()
        if verbose: print(s)
        intcode.load_code_from_string(s)

        t0 = time.process_time()
        print("Oxygen found after {} steps".format(part1(intcode)))
        t1 = time.process_time()
        print('Part 1:','process time', t1-t0,'seconds')

        t2 = time.process_time()
        print("It takes {} minutes to fill the area with oxygen".format(part2()))
        t3 = time.process_time()
        print('Part 2: process time', t3-t2,'seconds')
        print('Map:')
        print_cave(g_levellist)    

day15()
