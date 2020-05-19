class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(data)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        self.stack1.pop()

    def __str__(self):
        return self.stack1.__str__()


my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(8)
my_queue.enqueue(19)

my_queue.dequeue()

print(my_queue)


