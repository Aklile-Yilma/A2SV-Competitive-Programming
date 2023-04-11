"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employees_map = {}
        
        for employee in employees:
            employees_map[employee.id] = employee
            
        def dfs(id):
            
            importance = employees_map[id].importance
            for neighbor in employees_map[id].subordinates:
                importance += dfs(neighbor)
                    
            return importance
            
        total = dfs(id)
        
        return total
        