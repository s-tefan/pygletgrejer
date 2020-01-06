# Advent of Code 2019 day 22

# card shuffling as affine functions in Z_p

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


# This dict gives the coefficients of a composite affine
# transformation with a single shuffling of each kind
# as the outer function
g_fcn_coeff_dict = { \
    "deal with increment": (lambda inner,k,n: ((inner[0]*k)%n,(inner[1]*k)%n)),
    "deal into new stack": (lambda inner,k,n: ((-inner[0]-1)%n,n-inner[1])),
    "cut": (lambda inner,k,n: ((inner[0]-k)%n, inner[1]))
    }




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


def part1(commlist):
    # Does part 1 with affine function coefficients 
        n = 10007
        kort = 2019
        coeffs = coeffs_from_commlist(commlist,n)
        # coeffs are the coeffs for the affine function
        # for final position of a card as a function of
        # the original position
        k = (coeffs[0] + kort*coeffs[1]) % n
        print('Part 1: Card {} in position {}'.format(kort,k))

def part2(commlist):
        n = 119315717514047 # number of cards = modulus
        k = 101741582076661 # number of reshuffles
        coeffs = coeffs_from_commlist(commlist,n)
        # As in part1 after one shuffle process
        pcoeffs = power_coeffs(coeffs, k, n)
        # pcoeffs for k repeats
        invc = inv_coeffs(pcoeffs,n)
        # The inverse affine function yields
        # the original position as a function of the final
        pos = 2020
        k = (invc[0] + pos*invc[1]) % n
        print('In final position {}: card {}'.format(pos,k))


import sys, time


def main():
    with open("input22.txt", "r") as f:
        s = f.read()
        commlist = read(s)

        t0 = time.process_time()
        part1(commlist)
        t1 = time.process_time()
        print('Part 2:', 'process time', t1-t0, 'seconds')
        t2 = time.process_time()
        part2(commlist)
        t3 = time.process_time()
        print('Part 1:', 'process time', t1-t0, 'seconds')

main()