# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = ''
    
    for i in range(1, len(food)):  
        if food[i] > 1:    
            for j in range(food[i] // 2): 
                answer = answer + str(i)
    
    answer += '0' + answer[::-1]  

    return answer