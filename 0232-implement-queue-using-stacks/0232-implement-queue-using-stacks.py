class MyQueue:

    def __init__(self):
        self.stack = []
        self.removed_list = []

    def push(self, x: int) -> None:
        self.stack.append(x)        

    def pop(self) -> int:
        if not self.removed_list:
            for idx in range(len(self.stack)):
                self.removed_list.append(self.stack.pop())
        
        return self.removed_list.pop()
    
    def peek(self) -> int:
        if not self.removed_list:
            for idx in range(len(self.stack)):
                self.removed_list.append(self.stack.pop())
            
        return self.removed_list[-1]
        
    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.removed_list) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()