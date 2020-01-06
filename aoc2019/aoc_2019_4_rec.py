

# kombinatoriskt borde man fixa om man delar upp i fall 
# med och utan dubbel för olika antal siffror
# Alla olika C(10,n)
# Alla, ev lika C(10+n-1,9), placera ut 10-1 avdelare för 10 fack,
# med totalt n platser utöver avdelarna.
# ex: xx||x||xxx||||| för 002444

# låt minsta siffran vara 0 och största m = b-1
# När det gäller växande följder:
# Låt antalet s(n,d) strängt växande sifferföljder med n siffror efter en siffra d så har vi
# s(n,m) = 0
# s(0,d) = 0
# s(n,d) = \sum_{e=d+1}^9 s(n-1,e) 
# för växande, ej nödvv strängt växande, antal i(n,d)
# i(n,9) = 1
# i(0,d) = 0
# i(n,d) = \sum_{e=d}^9 i(n-1,e)


def output(s):
    print(s)
    pass

def gen_strict_inc(s,n,d,b,interval=None):
    if interval == None:
        interval = [0,b**n-1]
    if d == b :
        return 0 
    elif n == 0 :
        if interval[0] <= int(s) <= interval[1]:
            output(s)
            return 1
        else:
            return 0
    else:
        ss = 0
        for e in range(d+1,b):
            outstr = s + str(e)
            ss += gen_strict_inc(outstr, n-1, e, b, interval)
        return ss

def gen_inc(s,n,d,b,interval=None):
    if interval == None:
        interval = [0,b**n-1]
    m = b
    if d == m :
        return 0 
    elif n == 0 :
        if interval[0] <= int(s) <= interval[1]:
            output(s)
            return 1
        else:
            return 0
    else:
        ss = 0
        for e in range(d,b):
            outstr = s + str(e)
            ss += gen_inc(outstr, n-1, e, b, interval)
        return ss

def gen_no_triples_inc(s,n,d,b,interval=None):
    # yields the number of increasing digit sequences with one or more doubles but no triples
    if interval == None:
        interval = [0,b**n-1]
    if d == b :
        return 0 
    elif n == 0 :
        if interval[0] <= int(s) <= interval[1]:
            output(s)
            return 1
        else:
            return 0
    else:
        ss = 0
        if len(s)>=2 and s[-1]==s[-2]:
            start = d+1
        else:
            start = d
        for e in range(start,b):
            outstr = s + str(e)
            ss += gen_no_triples_inc(outstr, n-1, e, b, interval)
        return ss


#print(gen_strict_inc('',3,-1,10))

#print(gen_no_triples_inc('',6,0,10))

#quit()

interval = [156218,652527]
no_inc = gen_inc('',6,0,10,interval)
no_str_inc = gen_strict_inc('',6,0,10,interval)
print(no_inc,no_str_inc)
print(no_inc-no_str_inc)

# Äh, det var ju inte som nedan man skulle ha det i del 2
# Den är kvar att göra, alltså
no_no_trip = gen_no_triples_inc('',6,0,10,interval)
print(no_no_trip, no_str_inc)
print(no_no_trip-no_str_inc)
