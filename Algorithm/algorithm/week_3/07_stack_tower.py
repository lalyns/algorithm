top_heights = [6, 9, 5, 7, 4]
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

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()

        for index in range(len(heights)-1, -1, -1):
            if heights[index] > height :
                answer[len(heights)] = index + 1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))