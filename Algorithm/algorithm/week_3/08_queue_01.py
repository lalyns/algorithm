class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new = Node(value)
        # new.data = value
        # new.next = None

        if self.is_empty() :
            self.head = new
            self.tail = new
            return

        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if self.is_empty() :
            return "Queue is Empty!"
                
        result = self.head
        self.head = self.head.next

        return result.data

    def peek(self):
        if self.is_empty() :
            return "Queue is Empty!"

        return self.head.data

    def is_empty(self):
        return self.head is None