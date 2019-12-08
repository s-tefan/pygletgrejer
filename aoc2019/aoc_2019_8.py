# Advent of Code 2019, day 8

def read_layer(input, n_rows, n_per_row):
    n_chars = n_rows*n_per_row
    return input.read(n_chars)

class DigitError(Exception):
    pass

def del1(f, debug=False):
    min_zeros = None
    result = None
    layercount=0
    while True:
        s = read_layer(f, 25, 6)
        if s in ['\n','']: break
        if debug: print(s,len(s))
        try:
            n_of_each = list(map(lambda d:s.count(d),['0','1','2']))
            if sum(n_of_each) != 150: raise DigitError
            if debug: print(n_of_each)
            if (min_zeros == None) or (n_of_each[0] < min_zeros):
                min_zeros = n_of_each[0]
                result = n_of_each[1]*n_of_each[2]
                index = layercount
        except DigitError as inst:
            print("För helvete!", type(inst))
        layercount += 1
        if debug: print(min_zeros, result, index)
    return result



def del2(f, debug=False):
    width = 25
    height = 6
    n_pixels = width*height
    image = ["2"]*(n_pixels)
    while True:
        s = read_layer(f, width, height)
        #if s in ['\n','']: break
        if len(s) < n_pixels: break
        if debug: print(s,len(s))
        for k in range(n_pixels):
            if image[k]=="2":
                image[k] = s[k]

    symb={"0":"x", "1":" ", "2":"0"}
    rs=""
    for k in range(height):
        for c in image[k*width:(k+1)*width]:
            rs+=symb[c]
        rs += '\n'

    return rs




with open("input8.txt","r") as f:
        print(del1(f))

with open("input8.txt","r") as f:
        print(del2(f))
