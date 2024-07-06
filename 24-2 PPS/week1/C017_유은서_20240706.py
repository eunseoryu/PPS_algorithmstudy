# problem url: https://leetcode.com/problems/second-largest-digit-in-a-string/
class Solution:
    def secondHighest(self, s: str) -> int:
        unique_digits = set([int(x) for x in s if x.isnumeric()])
        
        sorted_digits = sorted(unique_digits)
        
        if len(sorted_digits) >= 2:
            return sorted_digits[-2] 
        
        return -1  