class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary.sort()
        
        # sum the salaries in the list except the first and last salaries since they are min and max salaries
        summation = sum(salary[1:len(salary)-1])
        # total number of salaries added
        num_of_items = len(salary) - 2
        
        average = summation/num_of_items
        
        return average