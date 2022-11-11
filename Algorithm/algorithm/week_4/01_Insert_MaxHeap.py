#계층형 / 비선형 자료 구조

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        
        if len(self.items) < 3 :
            return
        
        index = len(self.items) - 1

        while index > 1:
            parentIndex = self.getParentIndex(index)

            if self.items[index] > self.items[parentIndex] :
                self.items[index], self.items[parentIndex] = self.items[parentIndex], self.items[index]
                index = parentIndex
            else :
                break

        return

    def getParentIndex(self, value):
        return value // 2

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!