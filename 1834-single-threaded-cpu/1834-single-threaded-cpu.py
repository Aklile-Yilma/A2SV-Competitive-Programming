class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for idx, task in enumerate(tasks):
            task.append(idx)
                                 
        tasks.sort(key=lambda t: t[0])    
        
        heap, order = [], []
        ptr = 0
        curr_time = tasks[0][0]
        
        while heap or ptr < len(tasks):
            while ptr < len(tasks) and curr_time >= tasks[ptr][0]:
                etime, ptime, index = tasks[ptr]
                heappush(heap, (ptime, index))             
                ptr += 1
            
            if heap:
                ptime, index = heappop(heap)
                order.append(index)
                curr_time += ptime
            else:
                curr_time = tasks[ptr][0]
                
                                 
        return order
                                 
                
                
        
        
                                 
                                
        
                                 
                