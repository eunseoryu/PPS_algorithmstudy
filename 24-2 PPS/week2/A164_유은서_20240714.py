# problem url:https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[0:i]:
            answer.append(i - s[0:i].rindex(s[i]))
        else:
            answer.append(-1)
    return answer