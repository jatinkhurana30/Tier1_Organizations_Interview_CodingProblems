class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.length = 1
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    current_node.next = Node(data)
                    self.tail = current_node.next
                    self.length += 1
                    break
                else:
                    current_node = current_node.next

    def __str__(self):
        list_items = []
        current_node = self.head
        while current_node is not None:
            list_items.append(current_node.data)
            current_node = current_node.next

        return list_items.__str__()

    def __len__(self):
        return self.length

    def search(self, data):

        if self.head.data == data:
            return 0

        search_index = 0
        current_node = self.head
        while current_node is not None:

            if current_node.data == data:
                return search_index

            current_node = current_node.next
            search_index += 1

        return -1

    def delete_by_index(self, index):

        if self.head is None:
            return 'Empty List'

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
            return data

        current_index = 0
        current_node = self.head
        previous_node = None
        while current_node is not None:

            if current_index == index:
                previous_node.next = current_node.next
                if current_index == self.length - 1:
                    self.tail = previous_node
                self.length -= 1
                return True

            current_index += 1
            previous_node = current_node
            current_node = current_node.next

    def get_head_and_tail(self):
        if self.head and self.tail:
            return f'{self.head.data} , {self.tail.data}'
        else:
            return None

    def insert(self, index, data):
        current_index = 0
        current_node = self.head

        while current_index != index - 1:
            current_index += 1
            current_node = current_node.next

        new_node = Node(data)
        next_node = current_node.next
        current_node = new_node
        current_node.next = next_node

    def reverse(self):

        if self.length == 1:
            return None

        self.tail = self.head
        current_node = self.head
        previous_node = None

        while current_node is not None:
            this_node = current_node
            current_node = current_node.next
            this_node.next = previous_node
            previous_node = this_node

        self.head = this_node


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.delete_by_index(0)

    def print(self):
        print(self.queue)


my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(7)
my_queue.enqueue(4)
my_queue.enqueue(8)

my_queue.print()

my_queue.dequeue()

my_queue.print()
