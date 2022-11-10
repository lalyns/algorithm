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

def get_linked_list_sum(linked_list_1, linked_list_2):

    #linkedlist to number
    number1 = linked_list_to_number(linked_list_1)
    number2 = linked_list_to_number(linked_list_2)

    return number1 + number2

def linked_list_to_number(linked_list):
    temp_node = linked_list.head
    number = 0
    while temp_node is not None:
        number = (number * 10) + temp_node.data
        temp_node = temp_node.next

    return number


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))