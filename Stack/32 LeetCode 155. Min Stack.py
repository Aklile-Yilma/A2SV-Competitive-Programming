class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_value:
            self.min_value.append(val)
        if(val < self.min_value[-1]):
            self.min_value.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if self.min_value[-1] == removed:
            self.min_value.pop()
        

    def top(self) -> int:
        if(len(self.stack) == 0):
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        #if the list is empty
        if not self.min_Value:
            return 0
        return self.min_value[-1]
        
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



