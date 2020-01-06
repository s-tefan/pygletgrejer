import time
import aoc_2019_intcode as ic

'''
Strategy: Try different directions in a breadth first traversion until oxygen system found
Saving a copy of the intcode program for each direction recursively
Part one: stop when oxygen is found
Part two: note at which level there are no branches left.
'''

# globals
verbose = False


def basis_seq(n, k):
    basic_block = [0]*k+[1]*k+[0]*k+[-1]*k
    repeated_block = basic_block*(n//(4*k)) +basic_block[:n-4*(n//(4*k))+1]
    return repeated_block[1:]


def fft(s):
    input = [int(c) for c in s]
    n = len(input)
    val = []
    for k in range(1,n+1):
        val.append(abs(sum(a*b for (a,b) in zip(input, basis_seq(n,k))))%10)
    return(val)


def part1(s):
    for k in range(100):
        fl = fft(s)
        s = ''.join(str(j) for j in fl)
        print(s)
    return s

def part2():
    return 0


def day16():
    with open("input16.txt", "r") as f:
        s = f.read()
        if verbose:
            print(s)
        #s = '80871224585914546619083218645595'
        #s = '12345678'
        #print(s.strip('\n'))
        t0 = time.process_time()
        print(part1(s.strip('\n'))[:8])
        t1 = time.process_time()
        print('Part 1:', 'process time', t1-t0, 'seconds')

        t2 = time.process_time()
        print("{}".format(part2()))
        t3 = time.process_time()
        print('Part 2: process time', t3-t2, 'seconds')


day16()
