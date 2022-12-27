class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary.sort()
        
        summation = sum(salary[1:len(salary)-1])
        print(summation)
        num_of_items = len(salary) - 2
        
        average = summation/num_of_items
        
        return average