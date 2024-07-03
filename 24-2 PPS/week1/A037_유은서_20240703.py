# problem url: https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        results = []

        for x in range(left , right + 1):
            if "0" in str(x): 
                continue
            val = x

            while val > 0:
                n = val % 10
                if x % n != 0:
                    val = -1
                    break
                val = val // 10

            if val != -1:
                results.append(x)
        
        return results
        