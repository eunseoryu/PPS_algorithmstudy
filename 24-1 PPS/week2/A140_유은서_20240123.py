def solution(nums):
    
    answer = len(nums)/2
    count = dict()
    
    for i in nums :
        if i in count:
            count[i] += 1
        else:
            count[i] = 0
    
    if len(count) < (len(nums)/2):
        answer = len(count)
    return answer