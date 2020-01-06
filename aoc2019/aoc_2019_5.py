# aoc_2019_5.py
import sys
import aoc_2019_intcode as ic


def day5():
    with open("input5.txt","r") as f:
        code = ic.Intcode()
        code.load_code_from_string(f.read())
        code.run()

def test2(code):
        intcode = ic.Intcode(code)
        intcode.run()

#test2([3,9,8,9,10,9,4,9,99,-1,8])
#test2([3,9,7,9,10,9,4,9,99,-1,8])
#test2([3,3,1108,-1,8,3,4,3,99])
#test2([3,3,1107,-1,8,3,4,3,99])
#test2([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
#test2([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
#test2([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])

day5()