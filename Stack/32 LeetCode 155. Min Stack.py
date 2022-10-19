class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack: # check if stack is non-empty

             # if current value is less than last minimum value: then append value
            self.min_val = min(self.min_stack[-1], val) #update min_stack accordingly
        else:
            self.min_val = val

        self.min_stack.append(self.min_val)
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        # pop from the min_stack because EVERYTIME its adding the latest minumum value
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]

        
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



