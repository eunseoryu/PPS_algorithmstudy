# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False 

    return not stack
