"""
leetcode problem: https://leetcode.com/problems/employee-importance/

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {emp.id : emp for emp in employees}

        def dfs(emp_id: int):
            employee = employee_dict[emp_id]
            total = employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)
            return total
        
        return dfs(id)
            