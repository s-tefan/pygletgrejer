from gauss_elim_latex import *

fr = Fracamente
preapa = [[0,1,2,1,0,0],[2,0,4,0,1,0],[4,3,0,0,0,1]]
apa = GaussMatrix([[fr(x).limit_denominator(1024) for x in row] for row in preapa])
print(apa.matrix_to_latex())
print(apa.swap_rows(0,1))
print(apa.mult_row(0,fr("1/2")))
print(apa.add_row(-4,0,2))
print(apa.add_row(-3,1,2))
print(apa.mult_row(2,fr("-1/14")))
print(apa.add_row(-2,2,0))
print(apa.add_row(-2,2,1))
print(apa.matrix_to_latex())


