import sys
import aoc_2019_intcode as ic

def dict_from_list(inlist):
    return { i : inlist[i] for i in range(len(inlist) ) }

def test2(code):
        intcode = ic.Intcode(code)
        intcode.run()

codelist=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#print(dict_from_list(codelist))


#test2(codelist)
#test2(dict_from_list(codelist))
#test2([1102,34915192,34915192,7,4,7,99,0])
#test2([104,1125899906842624,99])

def day9():
    with open("input9.txt","r") as f:
        intcode = ic.Intcode()
        s = f.read()
        print(s)
        stripsplitline = s.strip().split(',')
        #intcode.load_code(dict_from_list(list(map(int,stripsplitline))))
        intcode.load_code_from_string(s)
        intcode.run()

day9()