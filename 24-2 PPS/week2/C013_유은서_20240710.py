# problem url: https://leetcode.com/problems/distribute-candies/
# using set
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        return min(len(candyType) // 2, len(unique_candies))
