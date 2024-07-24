from sys import stdin

t = int(stdin.readline())  
cnt = 0

while cnt < t:
    k = int(stdin.readline())  
    n = int(stdin.readline()) 
    array = [t for t in range(1, n+1)]
  
    for i in range(k):
        for j in range(1, n):
            array[j] += array[j-1]
    
    print(array[-1])
    cnt += 1
