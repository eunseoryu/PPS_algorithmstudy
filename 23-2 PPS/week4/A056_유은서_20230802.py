#Leetcode_496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                flag, value = 1, 0

                if nums1[i] == nums2[j]:
                    value = nums2[j]
                    
                    for n in range(j+1, len(nums2)):
                        if nums2[n] > value:
                            ans.append(nums2[n])
                            flag = 0
                            break
                    
                    if flag == 1:
                        ans.append(-1)
        return ans