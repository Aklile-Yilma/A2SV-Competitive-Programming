class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        
        if not self.isFull():
            self.q[self.front] = value
            self.front = (self.front + 1) % self.k
            self.size += 1
            return True
            
        return False
        

    def insertLast(self, value: int) -> bool:
        
        if not self.isFull():
            self.q[self.rear] = value
            self.rear = (self.rear - 1) % self.k
            self.size += 1
            return True
        return False
    
    def deleteFront(self) -> bool:
        
        if not self.isEmpty():
            self.front = (self.front - 1) % self.k
            self.size -= 1
            return True
        
        return False
        
    def deleteLast(self) -> bool:
        
        if not self.isEmpty():
            self.rear = (self.rear + 1) % self.k
            self.size -= 1
            return True
        
        return False

    def getFront(self) -> int:
        
        if not self.isEmpty():
            return self.q[(self.front - 1) % self.k]
        
        return -1

    def getRear(self) -> int:
        
        if not self.isEmpty():
            return self.q[(self.rear + 1) % self.k]
        
        return -1
        
    def isEmpty(self) -> bool:
        
        return self.size == 0
        

    def isFull(self) -> bool:
        
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()