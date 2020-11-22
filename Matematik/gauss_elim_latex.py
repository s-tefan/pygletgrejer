# Project goal:
# Present a series of row operations on matrices
# to be used with LaTeX package gauss

import fractions

class GaussMatrix:
    elem_sep_str = " & "
    row_sep_str = " \\\\\n"
    end_str = "\n"
    indent_str = " "*4
    leadsto_str = "\n\\leadsto"
    
    
    def __init__(self, array):
        self.array = array
        self.rowops = []




    def inner_matrix_to_latex(self):
        s = ""
        a = self.array
        for row in a[:-1]: # All but the last row
            s += self.indent_str
            for elem in row[:-1]:
                s += "{}{}".format(elem, self.elem_sep_str)
            s += str(row[-1]) + self.row_sep_str
        row = a[-1] # Last row
        s += self.indent_str
        for elem in row[:-1]:
            s += "{}{}".format(elem, self.elem_sep_str)
        s += str(row[-1])
        s += self.end_str
        if self.rowops:
            s += "\\rowops"
            for rowop in self.rowops:
                s += ("\\" + rowop)
        return s

    def matrix_to_latex(self):
        s = "\\begin{gmatrix}\n"
        s += self.inner_matrix_to_latex()
        s += "\\end{gmatrix}"
        return s


    def add_row(self, k, a, b):
        self.rowops.append("add[{}]{{{}}}{{{}}}".format(k,a,b))
        s = self.matrix_to_latex()
        self.rowops = []
        ar = self.array
        for i in range(len(ar[a])):
            ar[b][i] += k*ar[a][i]
        s += self.leadsto_str
        return s

    def swap_rows(self, a, b):
        self.rowops.append("swap{{{}}}{{{}}}".format(a,b))
        s = self.matrix_to_latex()
        self.rowops = []
        ar = self.array
        temp = ar[a]
        ar[a] = ar[b]
        ar[b] = temp
        s += self.leadsto_str
        return s

    def mult_row(self, r, k):
        self.rowops.append("mult{{{}}}{{\cdot {}}}".format(r, k))
        s = self.matrix_to_latex()
        self.rowops = []
        ar = self.array
        ar[r] = [k*x for x in ar[r]]
        s += self.leadsto_str
        return s


fr = fractions.Fraction
preapa = [[1,2,3],[0.1,-5,37]]
apa = GaussMatrix([[fr(x).limit_denominator(1024) for x in row] for row in preapa])
print(apa.array)
print(apa.swap_rows(0,1))
print(apa.add_row(-10,0,1))
print(apa.mult_row(0,10))
print(apa.mult_row(1,fr("1/52")))
print(apa.add_row(50,1,0))
print(apa.matrix_to_latex())


