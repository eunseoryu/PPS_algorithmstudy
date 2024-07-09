# problem url:https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        for c in range(len(matrix[0])):
            temp = []

            for r in range(len(matrix)):
                temp.append(matrix[r][c])
            
            result.append(temp)

        return result
        
