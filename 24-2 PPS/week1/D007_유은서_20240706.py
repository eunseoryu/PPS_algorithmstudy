# problem url: https://leetcode.com/problems/median-of-two-sorted-arrays/
# brute-force method
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()

        if len(num) % 2 != 0:
            return float(num[len(num) // 2])
        else:
            return (float(num[len(num) // 2 - 1]) + float(num[len(num) // 2])) / 2.0
        