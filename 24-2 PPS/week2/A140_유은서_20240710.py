# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    unique_nums = set(nums)
    
    return min(len(nums) // 2, len(unique_nums))