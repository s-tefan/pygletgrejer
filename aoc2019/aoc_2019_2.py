# aoc_2019_2.py
import sys

def runcode(opcode):
    pos=0
    while(opcode[pos]!=99):
        if opcode[pos]==1:
            opcode[opcode[pos+3]]\
                =opcode[opcode[pos+1]]\
                +opcode[opcode[pos+2]]
            pos+=4
        elif opcode[pos]==2:
            opcode[opcode[pos+3]]\
                =opcode[opcode[pos+1]]\
                *opcode[opcode[pos+2]]
            pos+=4
        else:
            raise ValueError

""" test = [1,9,10,3,2,3,11,0,99,30,40,50]
runcode(test)
print(test)
 """

def fixinput(line):
    strippedline = line.strip().split(',')
    return list(map(int,strippedline))

def uppgift1():
    for line in sys.stdin:
        opcode=fixinput(line)
        print(opcode)
        opcode[1:3]=[12,2]
        print(opcode)
        runcode(opcode)
        print(opcode)
        print(opcode[0])


def uppgift2():
    pass   
    for line in sys.stdin:
        opcodeorig=fixinput(line)
        for noun in range(100):
            for verb in range(100):
                opcode=opcodeorig.copy()
                opcode[1:3]=[noun,verb]
                runcode(opcode)
                if opcode[0]==19690720:
                    print(noun, verb)
                    print(100*noun+verb)


uppgift2()