# The function reduce(A) reduces a matrix A
# represented as a list of lists of same length
# into a rowequivalent row echelon matrix

# Some auxillary functions

def pivot(A):
    # permute the rows of A so that the first row
    # has the largest leading element
    firstrow=A[0]
    for rownum in range(1,len(A)):
        row = A[rownum]
        if abs(row[0])>abs(firstrow[0]):
            A[0]=row
            A[rownum]=firstrow
            firstrow=row

def multiplyby(row,k):
    for i in range(len(row)):
        row[i]=k*row[i]

def rowsubtract(row,byrow,k=1):
    for i in range(len(row)):
        row[i]-=k*byrow[i]

# The main function
def reduce(A, makeUnitLeaders=False):
    if A:
        if A[0]:
            pivot(A)
            pivotval=A[0][0]
            if pivotval!=0:
                firstrow=A[0]
                # 
                if makeUnitLeaders: multiplyby(firstrow,1/pivotval)
                for i in range(1,len(A)):
                    if makeUnitLeaders: 
                        rowsubtract(A[i],firstrow,A[i][0])
                    else:
                        rowsubtract(A[i],firstrow,A[i][0]/pivotval)
                # strip first row and first column
                # from A to make B
                B=[]
                for row in A[1:]:
                    B.append(row[1:])
                # reduce recurs1vely
                reduce(B,makeUnitLeaders)
                # put it back
                for i in range(len(B)):
                    A[1+i][1:]=B[i]
            else:
                # strip first column, which is null
                B=[]
                for row in A:
                    B.append(row[1:])
                # reduce recursively
                reduce(B,makeUnitLeaders)
                # put it back
                for i in range(len(B)):
                    A[i][1:]=B[i]




    # if A or its first line is empty, do nothing

def matrixprint(A):
    for row in A:
        print(row)


A=[[0,1,2,3,2,2,2],[1,2,3,4,1,1,1],[2,3,4,5,1,1,1],[3,4,5,6,0,0,2]]
matrixprint(A)
print()
reduce(A)
matrixprint(A)
print()
reduce(A,True)
matrixprint(A)