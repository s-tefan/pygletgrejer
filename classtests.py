class Ap:
    def __init__(self, n):
        self.n = n

    def __lt__(self, other):
        return self.n < other.n

    def __ge__(self, other):
        return self.n >= other.n

if __name__ == '__main__':
    fyra = Ap(4)    
    four = Ap(4)
    sex = Ap(6)
    print(fyra<sex, fyra>sex, fyra<=fyra, fyra>=fyra, \
        fyra>=sex, sex>=fyra, fyra<=sex, sex<=fyra, fyra == fyra, fyra==four)
    # varför funkar > och <=? det ska inte finnas 'swapping' i python3

