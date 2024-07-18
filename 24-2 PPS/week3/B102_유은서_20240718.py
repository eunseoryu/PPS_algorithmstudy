class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_num1 = set(nums1)
        unique_num2 = set(nums2)
        return list(unique_num1.intersection(unique_num2))