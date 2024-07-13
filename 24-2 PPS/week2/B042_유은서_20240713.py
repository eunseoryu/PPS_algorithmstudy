# problem url:https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        m, c, D = 0, 0, {'L':1, 'R':-1}
        for x in s:
            c = c + D[x]
            if c == 0: m = m +1
        
        return m
    
        