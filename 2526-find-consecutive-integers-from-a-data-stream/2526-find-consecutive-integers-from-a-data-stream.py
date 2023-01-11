class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.currIdx = -1
        self.lastIdx = -1
        
    def consec(self, num: int) -> bool:
        
        self.currIdx += 1
        if num != self.value:
            #reset last idx to current idx if num != value
            self.lastIdx = self.currIdx
        
        # window must be greater or equal to k
        return self.currIdx - self.lastIdx >= self.k
    

        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)