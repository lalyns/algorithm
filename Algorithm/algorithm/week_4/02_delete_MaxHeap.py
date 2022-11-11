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

    def delete(self):
        length = len(self.items)

        if length == 1 :
            return "Heap is Empty"

        lastIndex = len(self.items) - 1
        
        # 루트 노드를 변수에 담는다
        rootNode = self.items[1]

        # 루트 노드와 마지막 노드를 변경한다
        self.items[1] , self.items[lastIndex] = self.items[lastIndex] , self.items[1]
        # 마지막 노드를 삭제한다
        del self.items[lastIndex]

        curIndex = 1
        length = len(self.items)
        
        while True :
            leftIndex = curIndex * 2
            rightIndex = curIndex * 2 + 1

            # 현재 노드가 리프노드일 경우
            if leftIndex > length-1 and rightIndex > length-1 :
                break
            
            # 현재 노드의 자식노드가 왼쪽만 있는 경우
            elif leftIndex == length-1 and rightIndex > length-1 :
                if self.items[curIndex] < self.items[leftIndex] :
                    self.items[curIndex], self.items[leftIndex] = self.items[leftIndex], self.items[curIndex]
                    break                        
            
            # 현재 노드의 자식노드가 존재하고, 오른쪽 자식노드가 마지막 노드일 경우
            elif rightIndex == length-1 :
                if self.items[leftIndex] > self.items[rightIndex] :
                    self.items[curIndex], self.items[leftIndex] = self.items[leftIndex], self.items[curIndex]
                    break                    
                else :
                    self.items[curIndex], self.items[rightIndex] = self.items[rightIndex], self.items[curIndex]
                    break

            # 현재 노드가 두 자식 노드보다 클 경우
            if self.items[curIndex] >= self.items[leftIndex] and self.items[curIndex] >= self.items[rightIndex]:
                break
            
            # 오른쪽 자식 노드보다 현재노드가 작을 경우
            elif self.items[curIndex] >= self.items[leftIndex] and self.items[curIndex] < self.items[rightIndex] :
                self.items[curIndex], self.items[rightIndex] = self.items[rightIndex], self.items[curIndex] 
                curIndex = rightIndex

            # 왼쪽 자식 노드보다 현재 노드가 작을 경우
            elif self.items[curIndex] < self.items[leftIndex] and self.items[curIndex] >= self.items[rightIndex] :
                self.items[curIndex], self.items[leftIndex] = self.items[leftIndex], self.items[curIndex]
                curIndex = leftIndex
                # 두 자식 노드를 비교, 왼쪽이 클 경우

            # 두 자식노드보다 모두 작을 경우
            else :

                # 두 자식노드 끼리 비교 했을 때 왼쪽이 클 경우
                if self.items[leftIndex] > self.items[rightIndex] :
                    self.items[curIndex], self.items[leftIndex] = self.items[leftIndex], self.items[curIndex]
                    curIndex = leftIndex

                # 두 자식노드 끼리 비교 했을 때 오른쪽이 클 경우
                else :
                    self.items[curIndex], self.items[rightIndex] = self.items[rightIndex], self.items[curIndex] 
                    curIndex = rightIndex

        # 구현해보세요!
        return rootNode  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]