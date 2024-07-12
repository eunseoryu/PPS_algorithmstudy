# problem url:https://leetcode.com/problems/maximum-69-number/
class Solution:
    def maximum69Number (self, num: int) -> int:
        numlist = list(str(num))
        if '6' in numlist:
            for i in range(len(numlist)):
                if numlist[i] == '6':
                    numlist[i] = '9'
                    return int(''.join(numlist))
        else:
            return num

            