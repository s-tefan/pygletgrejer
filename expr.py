class Expr:
    pass
    def distribute_once(self):
        return(self)
    def distribute(self):
        return(self)
    def str_infix(self):
        pass

class Const(Expr):
    def __init__(self, val):
        self.val = val
    def str_infix(self):
        return str(self.val)


class Var(Expr):
    def __init__(self,name):
        self.name = name
    def str_infix(self):
        return str(name)

class Plus(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
    def str_infix(self):
        return str( '(' + self.l.str_infix() + ' + '+ self.r.str_infix()+')')

class Times(Expr):
    def __init__(self,l,r):
        self.l = l
        self.r = r
    def str_infix(self):
        return str('('+self.l.str_infix()+'.'+self.r.str_infix()+')')
    def distribute_once(self):
        if isinstance(self.l, Plus):
            print('Distribute!')
            distr = Plus(
                Times(self.l.l, self.r),
                Times(self.l.r, self.r))
            return distr
        elif isinstance(self.r, Plus):
            print('Distribute!')
            distr = Plus(
                Times(self.l, self.r.l),
                Times(self.l, self.r.r))
            return distr
        else:
            return self
    def distribute(self):
        d = self.distribute_once()
        if isinstance(d, Plus):

apa = Times(Plus(Const('a'),Const('b')),Plus(Const('c'),Const('d')))
print(apa.str_infix())
bepa = apa.distribute()
print(apa.str_infix())
print(bepa.str_infix())

