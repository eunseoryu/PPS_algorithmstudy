# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42885?language=python3
def solution(people, limit):
    answer = 0
    
    high = len(people) -1
    low = 0
    people.sort()
    
    while high > low:
        if(people[low] + people[high] <= limit):
            answer = answer + 1
            low = low + 1
        high = high - 1
    
    return len(people) - answer