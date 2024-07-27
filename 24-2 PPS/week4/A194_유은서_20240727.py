n = int(input())  

for i in range(n):
    arr = list(map(int, input().split())) 
    print(f"Case #{i + 1}: {arr[0]} + {arr[1]} = {arr[0] + arr[1]}")  
