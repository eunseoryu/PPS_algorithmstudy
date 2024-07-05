# problem url:https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = int(''.join(map(str, digits))) + 1
        return [int(x) for x in str(temp)]
        