class MyQueue:

    def __init__(self):
        self.queue = []


    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)


    def peek(self) -> int:
        return self.queue[0]


    def empty(self) -> bool:
        return len(self.queue) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# Runtime: 38 ms, faster than 72.64% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 13.9 MB, less than 74.91% of Python3 online submissions for Implement Queue using Stacks.
