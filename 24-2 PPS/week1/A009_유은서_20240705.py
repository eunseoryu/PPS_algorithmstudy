# problem url:https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3

def solution(s):
#     answer = True
#     if len(s) != 4 and len(s) != 6:
#         return False
#     str1 = list(s)
#     for x in str1:
#         if (x >= "a" and x <= "z") or (x >= 'A' and x <= 'Z'):
#             return False


    return s.isdigit() and len(s) in [4,6]
    
    return answer