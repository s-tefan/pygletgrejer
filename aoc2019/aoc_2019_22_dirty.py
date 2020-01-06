# Advent of Code 2019 day 22

# card shuffling as arithmetics in Z_p

verbose = False

def inv(x,n):
# Multiplicative inverse mod n by euclids alg.
    qlist = []
    rlist = [n,x]
    r=1
    while r != 0:
        q = rlist[-2]//rlist[-1]
        r = rlist[-2]%rlist[-1]
        qlist.append(q)
        rlist.append(r)
    qlist.pop()
    b = -qlist.pop()
    a = 1
    while qlist:
        q = qlist.pop()
        a0,b0 = a,b
        a = b0
        b = (a0 - q*b0) % n
    return b

'''
# Alternatively, for prime p
def inv(x,n):
    return pow(x,n-2,n)
'''

def read(instr):
    # take indata as a string and make into a list
    # of (operation, parameter)
    lines = instr.split('\n')
    commlist=[]
    for line in lines:
        linecomm = ""
        for comm in comms:
            if line[:len(comm)] == comm:
                linecomm = comm
                par = line[len(comm):]
        try: intpar = int(par)
        except: intpar = None
        commlist.append((linecomm,intpar))
    return commlist


comms = ["deal with increment", "deal into new stack","cut"]

g_fcndict = { \
    "deal with increment": (lambda x,k,n: (x*k)%n),
    "deal into new stack": (lambda x,k,n: (-x-1)%n),
    "cut": (lambda x,k,n: (x-k)%n )
    }

g_invfcndict = {
    "deal with increment": (lambda x,k,n: (x*inv(k,n))%n),
    "deal into new stack": (lambda x,k,n: (-x-1)%n),
    "cut": (lambda x,k,n: (x+k)%n )
    }

# This dict gives the coefficients of a composite affine
# transformation with a single shuffling of each kind
# as the outer function
g_fcn_coeff_dict = { \
    "deal with increment": (lambda inner,k,n: ((inner[0]*k)%n,(inner[1]*k)%n)),
    "deal into new stack": (lambda inner,k,n: ((-inner[0]-1)%n,n-inner[1])),
    "cut": (lambda inner,k,n: ((inner[0]-k)%n, inner[1]))
    }



def doit(commlist,n,kort):
    # does part one in two different ways        
        # Version 1
        # generate the shuffled deck
        # then look up card
        cardlist = list(range(n))
        for comm in reversed(commlist):
            if comm[0] in comms:
                fcn = g_invfcndict[comm[0]]
                new_cardlist = [fcn(x,comm[1],n) for x in cardlist]
                cardlist = new_cardlist
                #print(comm,':',cardlist)
        if verbose: print(cardlist)
        print(cardlist.index(kort))

        # Version 2
        # does not generate the deck
        # tracks the positions through shuffling
        k = kort
        for comm in commlist:
            if comm[0] in comms:
                fcn = g_fcndict[comm[0]]
                k = fcn(k,comm[1],n)
                print(comm[0],comm[1],'Card',kort,'in position',k)



def coeffs_from_commlist(commlist,n):
    # The position a card is in after shuffeling is 
    # an affine function of the original position,
    # and so is its inverse
    # An affine function x -> a_0 + a_1 x
    # is determined by two coefficients
    # The composition of an affine function with 
    # a single shuffling is listed in g_fcn_coeff_dict
    coeffs=(0,1)
    for comm in commlist:
        if comm[0] in comms:
            fcn = g_fcn_coeff_dict[comm[0]]
            coeffs = fcn(coeffs,comm[1],n)
    return coeffs

def inv_coeffs(coeffs,n):
    ainv = inv(coeffs[1],n)
    return ((-ainv*coeffs[0])%n,ainv)

def power_coeffs(coeffs,k,n):
    cpow = pow(coeffs[1],k,n)
    cinv = inv(coeffs[1]-1,n)
    return ((coeffs[0]*(cpow-1)*cinv)%n, cpow)


def part1():
    with open("input22.txt", "r") as f:
        s = f.read()
        commlist = read(s)
        doit(read(s),10007,2019)

def test1():
    with open("test22.txt", "r") as f:
        s = f.read()
        commlist = read(s)
        for kort in range(10):
            doit(commlist,10,kort)


def test2():
    with open("test22.txt", "r") as f:
        n = 10
        s = f.read()
        commlist = read(s)
        coeffs = coeffs_from_commlist(commlist,n)
        invcoeffs = inv_coeffs(coeffs,n)
        for kort in range(10):
            k = (coeffs[0] + kort*coeffs[1]) % n
            print(coeffs)
            print('Card',kort,'in position',k)
        for pos in range(10):
            print((invcoeffs[0] + pos*invcoeffs[1]) % n, end=' ')        

def part1_2():
    # Does part 1 with affine function coefficients 
    with open("input22.txt", "r") as f:
        n = 10007
        s = f.read()
        commlist = read(s)
        coeffs = coeffs_from_commlist(commlist,n)
        kort = 2019
        k = (coeffs[0] + kort*coeffs[1]) % n
        print('Kort {} på position {}'.format(kort,k))

def part2():
    with open("input22.txt", "r") as f:
        n = 119315717514047 # number of cards = modulus
        k = 101741582076661 # number of shufflings
        s = f.read()
        commlist = read(s)
        coeffs = coeffs_from_commlist(commlist,n)
        coeffs = power_coeffs(coeffs, k, n)
        invc = inv_coeffs(coeffs,n)
        pos = 2020
        k = (invc[0] + pos*invc[1]) % n
        print(coeffs, invc, ((invc[0]+invc[1]*coeffs[0])%n,(invc[1]*coeffs[1])%n))
        print('In position {}: card {}'.format(pos,k))


import sys, time


#test1()
#part1()
#test2()
#part1_2()
t0 = time.process_time()
part2()
t1 = time.process_time()
print('Part 2:', 'process time', t1-t0, 'seconds')