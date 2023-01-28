class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        #sorting it makes it easily so that the largest and smallest are together on the boat
        people.sort()
        

        left = 0
        right = len(people) - 1 
        boats = 0
        
        
        while left <= right:
            if(people[left] + people[right] <= limit):
                # both pointers are moved
                boats +=1
                left += 1 
                right -= 1
            
            else:
                # only the right pointer is moved because that number is large and can't fit with the others since they are sorted
                boats += 1
                right -= 1
             
            
            
        return boats
            
                