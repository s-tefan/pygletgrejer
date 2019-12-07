
def number_of_passwords(n_of_digits,max):
    if n_of_digits==1:
        return None
        #blaj

# kombinatoriskt borde man fixa om man delar upp i fall 
# med och utan dubbel för olika antal siffror
# Alla olika C(10,n)
# Alla, ev lika C(10+n-1,9), placera ut 10-1 avdelare för 10 fack,
# med totalt n platser utöver avdelarna.
# ex: xx||x||xxx||||| för 002444

class PassordIterator:
    def __iter__(self,size=6,start=(0,)*size):
        check(start)
        self.word=list(start)

        
def check(word):
    double=False
    for k in range(len(word)-1):
        if word(k+1)>word(k):
            return False
        elif word(k+1)==word(k):
            double=True
    return double
    