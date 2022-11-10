class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None :
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None :
            cur = cur.next
        cur.next = Node(data)

    def print_all(self) :
        print("Start")
        cur = self.head
        while cur is not None :
            print(cur.data)
            cur = cur.next
        print("END")
        
    def getNode(self, index):
        count = 0
        node = self.head
        while   count < index - 1 :
            node = node.next
            count += 1
        return node
    
    def addNode(self, index, value):
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
            return

        prevNode = self.getNode(index-1)
        nextNode = prevNode.next
        prevNode.next = node
        node.next = nextNode

    def delNode(self, index):
        if index == 0:
            self.head = self.head.next
            return 

        prevNode = self.getNode(index - 1)
        prevNode.next = self.getNode(index).next


linked_list = LinkedList(3)
linked_list.append(6)
linked_list.append(5)
linked_list.append(2)
linked_list.append(7)
linked_list.append(1)
linked_list.append(9)

linked_list.addNode(3,15)
linked_list.print_all()

linked_list.delNode(8)
linked_list.print_all()
