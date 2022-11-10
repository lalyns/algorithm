class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # pop 기능 구현
    def pop(self):
        if self.is_empty() :
            return "Stack is empty!"
        temp = self.next
        self.head = self.next
        return temp

    def peek(self):
        if self.is_empty() :
            return "Stack is empty!"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None