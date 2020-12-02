
class BinaryTree:
    breadth_first = 1
    width_first = 2

    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.iteration_type = None

    def add_left(self, left):
        self.left = left
        return self
    
    def add_right(self, right):
        self.right = right
        return self
    
    def add_childer(self, left, right):
        self.add_left(left)
        self.add_right = right
        return self

    def set_value(self, value):
        self.value = value
        return self

    def __iter__(self):
        self.left_done = False
        self.right_done = False
        return self
    '''
    def iter_breadth_first(self):
        return self

    def iter_depth_first(self):
        return self
    '''

    def __next__(self):
        if self.iteration_type == self.breadth_first:
            pass # to be implemented
        elif self.iteration_type == self.depth_first:
            pass # to be implemented
        else:
            raise Exception("Iteration type not set")


