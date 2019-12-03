class stekafibo:
    def __init__(self,f0,f1,n=float('inf')):
        self.f0=f0
        self.f1=f1
        self.n=n

    def __iter__(self):
        return self

    def next(self):
        if self.n<0:
            raise StopIteration()
        else:
            f2=self.f0+self.f1
            self.f0=self.f1
            self.f1=f2
            self.n-=1
            return self.f0

for apa in stekafibo(0,1,20):
    print(apa)


    
    
