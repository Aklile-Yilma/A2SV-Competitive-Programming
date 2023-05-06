class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []  # Min Heap
        for num in nums:
            heapq.heappush(self.minHeap, num)   # adding all elements to min heap
            
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)         # Only keeping k maximum elements
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)       # first add to min heap
        
        if len(self.minHeap) > self.k:          # if length greater pop minimum element as root is the min
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]                  # root is minHeap[0] as root is k'th max
        
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)