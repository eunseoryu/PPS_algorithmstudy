def solution(numbers):
    numbers.sort(reverse = False)
    a = list(range(10))
    for x in numbers:
        idx = a.index(x)
        a[idx] = 0
    
    
    answer = sum(a)
    return answer