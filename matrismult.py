dimerror=Exception('Uncompatible matrix dimensions')

def mdim(matris):
    r=len(matris)
    c=len(matris[0])

    return (r,c)


def madd(a,b):
    adim=mdim(a)
    bdim=mdim(b)
    if adim!=bdim: raise dimerror
    c=[]
    for rnum in range(adim[0]):
        row=[]
        for cnum in range(adim[1]):
            row.append(a[rnum][cnum]+b[rnum][cnum])
        c.append(row)
    return c

def mmult(a,b):
    (ra,ca)=mdim(a)
    (rb,cb)=mdim(b)
    if ca!=rb: raise dimerror
    if ra==1 and ca==1 and rb==1 and cb==1:
        return [[a[0][0]*b[0][0]]]
    else:
        [a11,a12,a21,a22]=msplit(a)
        [b11,b12,b21,b22]=msplit(b)
        ## Följande blir inte bra, det blir ju matriser i matriser. Får fixas
        return [[
            madd(mmult(a11,b11),mmult(a12,b21)),
            madd(mmult(a11,b12),mmult(a12,b22))],
            [
            madd(mmult(a21,b11),mmult(a22,b21)),
            madd(mmult(a21,b12),mmult(a22,b22))]
            ]

def msplit(m):
    (r,c)=mdim(m)
    newr=r//2
    newc=c//2
    mleft=[]
    mright=[]
    for row in m:
        mleft.append(row[:newc])
        mright.append(row[newc:])
    return [mleft[:newr],mright[:newr],
            mleft[newr:],mright[newr:]]
    

print(msplit([[1,2,3],[4,5,6],[7,8,9]]))
a=[[1,2],[3,4]]
b=[[1,1],[1,-1]]
print(a,'*',b,'=',mmult(a,b))
