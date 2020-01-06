import aoc_2019_intcode as ic

def part1():
    with open("input13.txt","r") as f:
        intcode = ic.IntcodeIO()
        s = f.read()
        intcode.load_code_from_string(s)
        
        out = intcode.run_io([])

        screen = {}
        while out:
            xpos = out.pop(0)
            ypos = out.pop(0)
            tile_id = out.pop(0)
            screen[(xpos,ypos)] = tile_id

        print(list(screen.values()).count(2))

part1()

#
    
