class MedianFinder:

    def __init__(self):
        # contains small half
        self.maxHeap = []
        #contains large half
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        
        # arbitrarly push to the heap that contains the smaller half
        heappush(self.maxHeap, -1 * num)
        
        # case: if maxHeap has a larger value than minHeap
        if (self.maxHeap and self.minHeap and (-1 * self.maxHeap[0]) > self.minHeap[0]):
            val = -1 * heappop(self.maxHeap)
            heappush(self.minHeap, val)
            
        #Handle uneven size
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heappop(self.maxHeap)
            heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()