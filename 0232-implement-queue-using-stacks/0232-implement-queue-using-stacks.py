class MyQueue(object):

    def __init__(self):
        # Initialize two arrays or stacks
        self.inn = [] # the stack when we want to push queue
        self.out = [] # the stack when we want to pop
        

    def push(self, x):
        self.inn.append(x) 
        

    def pop(self):
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop()) 
        return self.out.pop()


    def peek(self):
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop())
        return self.out[len(self.out)-1]
        

    def empty(self):
        return len(self.inn) == 0 and len(self.out) == 0