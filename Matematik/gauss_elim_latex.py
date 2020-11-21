# Project goal:
# Present a series of row operations on matrices
# to be used with LaTeX package gauss

class GaussMatrix:
    elem_sep_str = " & "
    row_sep_str = " \\\\\n"
    end_str = "\n"
    
    
    def __init__(self, array):
        self.array = array




    def matrix_to_latex(self):
        s = ""
        a = self.array
        for row in a[:-1]: # All but the last row
            for elem in row[:-1]:
                s += "{}{}".format(elem, self.elem_sep_str)
            s += str(row[-1]) + self.row_sep_str
        row = a[-1] # Last row
        for elem in row[:-1]:
            s += "{}{}".format(elem, self.elem_sep_str)
        s += str(row[-1])
        s += self.end_str
        return s



apa = GaussMatrix([[1,2,3],[0.1,-5,37]])
print(apa.matrix_to_latex())

        