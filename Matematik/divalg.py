


# long division algorithm for lists of coefficients
# list[k] is the k:th degree coefficient

def long_divide(dividend, divisor):
    q = dividend[-1]/divisor[-1]
    qdeg = len(dividend)-len(divisor)
    remainder = [dividend[-1-k]-q*divisor[-1-k] \
        for k in range(1,len(divisor))]
        # Nu saknas delen av resten där det inte finns divisorkoeffs
        # behöver komplettera med dividendens koeffs där
    return q, qdeg, remainder

bla = long_divide([2,3,4,5],[1,1,2])
print(bla)

