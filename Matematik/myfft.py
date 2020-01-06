import cmath
import operator

def fft(x):
    # x is a list of 2-power length of real or complex values
    nn = len(x)
    if nn==1:
        return x[0:1]
    else:
        evens=x[0::2]
        odds=x[1::2]
        hcirc = list(map(
            lambda k: -2*cmath.pi*1j*k/nn,
            list(range(nn//2))
            ))
        fftevens = fft(evens)
        fftodds = fft(odds)
        fftodds1 =  map(operator.mul,hcirc,fftodds)
        fft1 = list(map(operator.add,fftevens,fftodds))
        fft2 = list(map(operator.sub,fftevens,fftodds))
    return fft1+fft2

x=[1,-1,1,-1]
fftx=fft(x)
fft2x=fft(fftx)
print(fftx,fft2x)
