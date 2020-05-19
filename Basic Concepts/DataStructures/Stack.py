class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        self.stack.pop()

    def __str__(self):
        return self.stack.__str__()


my_stack = Stack()

my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.pop()
print(my_stack)

