# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/133499
def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        idx = 0
        isspeak = True
        last_word = ""  
        
        while idx < len(s) and isspeak:
            matched = False
            for sub in possible:
                if s[idx:idx+len(sub)] == sub:
                    if last_word == sub:  
                        isspeak = False
                        break
                    idx += len(sub)  
                    last_word = sub  
                    matched = True
                    break
            if not matched:
                isspeak = False
        
        if isspeak and idx == len(s):
            answer += 1
                
    return answer

