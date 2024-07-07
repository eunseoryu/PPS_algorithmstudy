# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    temp = []
    prev = -1
    
    for x in arr:
        if x != prev:
            temp.append(x)
        prev = x
            
    
    return temp