import aoc_2019_intcode as ic


def day11():
    with open("input11.txt", "r") as f:
        intcode = ic.IntcodeIO()
        s = f.read()
        #print(s)
        stripsplitline = s.strip().split(',')
        # intcode.load_code(dict_from_list(list(map(int,stripsplitline))))
        intcode.load_code_from_string(s)

        white = set()
        black = set()
        pos = (0, 0)
        dir = (0, 1)
        white.add(pos)

        # white.add(pos)
        while True:
            color_white = int(pos in white)
            input = [color_white]
            output = intcode.run_io(input)
            # print(output)
            if output:
                if output[0] and not color_white:
                    white.add(pos)
                    if pos in black:
                        black.remove(pos)
                elif color_white:
                    white.remove(pos)
                    black.add(pos)
                if output[1]:
                    dir = (dir[1], -dir[0])
                else:
                    dir = (-dir[1], dir[0])
                pos = tuple(sum(x) for x in zip(pos, dir))
                # print(pos)
            else:
                break
        print(len(white)+len(black))
        white_x = tuple(p[0] for p in white)
        white_y = tuple(p[1] for p in white)
        print('x:', min(white_x), max(white_x),
              'y:', min(white_y), max(white_y), )
        for y in range(max(white_y), min(white_y)-1, -1):
            line = ''
            for x in range(min(white_x), max(white_x)+1):
                if (x, y) in white:
                    line += 'w'
                elif (x, y) in black:
                    line += '.'
                else:
                    line += ' '
            print(line)


day11()
