# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = ((price * (count * (count+1)/2)) - money)
    if answer < 0:
        return 0
    return answer