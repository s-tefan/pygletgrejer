
class Citer:
    k = 0.01
    def __iter__(self):
        self.c = 1/4
        return self
    
    def __next__(self):
        x = self.c
        self.c -= self.k*(self.c+2)
        return x


def mandel_it(z, c):
    return z**2 + c

it = Citer()
c_dict = {}
for c in it:
    z = [0]
    for k in range(10):
        z.append(mandel_it(z[-1], c))
    c_dict[c] = z
    print(c, z)
    if c < -1.99:
        break



