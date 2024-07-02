'''
problem link:https://leetcode.com/problems/pascals-triangle/
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascal = [[1]] 
        
        for x in range(1, numRows):
            temp = [1] 
            prev = pascal[x - 1]

            for i in range(1, x):
                temp.append(prev[i - 1] + prev[i])  
            
            temp.append(1)
            pascal.append(temp) 
        
        return pascal
