import sys

debug = False
#debug = True


# Implements intcode as a python class up to day 9

class Intcode:

    def __init__(self, code = [], pos = 0):
        self.code = code
        self.pos = pos
        self.relative_base = 0
        # A dictionary of operations for opcodes
        self.op_dict = {
            1: self.add,
            2: self.mult,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.relative_base_offset,
            99: self.terminate,
        }

    def copy(self):
        intcodecopy = Intcode(code = self.code.copy(), pos = self.pos)
        intcodecopy.relative_base = self.relative_base
        return intcodecopy

    def interpret_parameters(self, n_params, modes):
        # Interprets parameters for an opcode
        inparams = []
        for k in range(n_params): # slice does not work if the code is a dict
            inparams.append(self.lookup(self.pos+1+k))
        pos = [None]*n_params
        for k in range(n_params):
            mode = modes%10
            modes = modes//10
            if mode == 0:
                pos[k] = inparams[k]
            elif mode == 1:
                pos[k] = self.pos+1+k
            elif mode == 2:
                pos[k] = inparams[k] + self.relative_base
            else:
                pass
        return pos

    def lookup(self,pos):
        # Looks up code at position pos
        try:
            return self.code[pos]
        except IndexError:
            return 0 # Code is a list and pos is outside index range
        except KeyError:
            return 0 # Code is a dict and pos is not a key 

    def store(self,pos,val):
        # Stores val at position pos in code
        try:
            self.code[pos]=val
        except IndexError:
            # If code is a list and pos is outside index range
            # raise IndexError('Trying to store code outside list. Try init code as dict.')
            print('Changing stored code from list to dict', file=sys.stderr)
            self.make_code_dict() # Make code a dict instead of a list
            # May want to refactor into extending list instead if not becoming sparse
            self.store(pos,val)

    def make_code_dict(self):
        # changes code storage from list to dict
        dict_code = { i : self.code[i] for i in range(len(self.code) ) }
        self.code = dict_code

    def load_code(self, code, pos=0):
        # loads code into intcode object
        self.code = code
        self.pos = pos

    def load_code_from_string(self,codestring):
        # loads code (as string) into intcode object
        stripsplitline = codestring.strip().split(',')
        self.load_code(list(map(int,stripsplitline)))
    
    def run(self):
        # runs the intcode
        while True:
            if debug: print(self.code)
            opcode = self.lookup(self.pos)
            if debug: print('pos:', self.pos, ' opcode:', opcode, ' rel_base:', self.relative_base)
            op = self.op_dict[opcode%100]
            mode = opcode//100
            if not op(mode):
                break # run the op, break if program terminates

# operations for the different opcode
# returns True except for terminate()

    # 1
    def add(self, mode=0):
        par_pos = self.interpret_parameters(3,mode)
        self.store(par_pos[2], \
            self.lookup(par_pos[0]) + self.lookup(par_pos[1])
            )
        self.pos += 4
        return True

    # 2
    def mult(self, mode=0):
        par_pos = self.interpret_parameters(3,mode)
        self.store(par_pos[2], \
            self.lookup(par_pos[0]) * self.lookup(par_pos[1])
            )
        self.pos += 4
        return True
    
    # 3
    def input(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        self.store(par_pos[0], int(input('>')))
        self.pos += 2
        return True

    # 4
    def output(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        print(self.lookup(par_pos[0]))
        self.pos += 2
        return True

    # 5
    def jump_if_true(self,mode):
        par_pos = self.interpret_parameters(2,mode)
        if self.lookup(par_pos[0]):
            self.pos=self.lookup(par_pos[1])
        else:
            self.pos += 3
        return True

    # 6
    def jump_if_false(self,mode):
        par_pos = self.interpret_parameters(2,mode)
        if not self.lookup(par_pos[0]):
            self.pos=self.lookup(par_pos[1])
        else:
            self.pos += 3
        return True

    # 7
    def less_than(self,mode):
        par_pos = self.interpret_parameters(3,mode)
        if self.lookup(par_pos[0]) < self.lookup(par_pos[1]):
            self.store(par_pos[2], 1)
        else:
            self.store(par_pos[2], 0)
        self.pos += 4
        return True

    # 8
    def equals(self,mode):
        par_pos = self.interpret_parameters(3,mode)
        if self.lookup(par_pos[0]) == self.lookup(par_pos[1]):
            self.store(par_pos[2], 1)
        else:
            self.store(par_pos[2], 0)
        self.pos += 4
        return True

    # 9
    def relative_base_offset(self,mode):
        np = 1
        par_pos = self.interpret_parameters(np,mode)
        self.relative_base += self.lookup(par_pos[0])
        self.pos += (np + 1)
        return True

    # 99
    def terminate(self, mode=0):
        return False

class IntcodeIO(Intcode):

    NEEDS_INPUT = 2
    WRITE = 3

    output_buffer = []
    input_buffer = []

    def copy(self):
        intcodecopy = IntcodeIO(code = self.code.copy(), pos = self.pos)
        intcodecopy.relative_base = self.relative_base
        intcodecopy.input_buffer = self.input_buffer.copy()
        intcodecopy.output_buffer = self.output_buffer.copy()
        return intcodecopy


    def input(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        if self.input_buffer:
            self.store(par_pos[0], self.input_buffer.pop(0))
            self.pos += 2
            return True
        else:
            return self.NEEDS_INPUT

    def output(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        self.send(self.lookup(par_pos[0]))
        self.pos += 2
        return True

    def send(self, outp):
        self.output_buffer.append(outp)


    def run_io(self, inp):
        # runs the intcode with iterable input inp until next input
        # where outp is returned
        self.input_buffer = inp.copy()
        while True:
            if debug: print(self.code)
            opcode = self.lookup(self.pos)
            if debug: print('pos:', self.pos, ' opcode:', opcode, ' rel_base:', self.relative_base)
            op = self.op_dict[opcode%100]
            mode = opcode//100
            return_value = int(op(mode))
            if return_value == 0 : 
                outp = self.output_buffer.copy()
                self.output_buffer = []
                return outp 
#                break  # run the op, break if program terminates
            elif return_value == self.NEEDS_INPUT :
                outp = self.output_buffer.copy()
                self.output_buffer = []
                return outp 
