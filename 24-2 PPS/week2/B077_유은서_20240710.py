# def pibonacci(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     memo[n] = pibonacci(n-1, memo) + pibonacci(n-2, memo)
#     return memo[n]

def pibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a + b
    return b



if __name__ == "__main__":
    user_input = int(input())
    print(pibonacci(user_input))
    