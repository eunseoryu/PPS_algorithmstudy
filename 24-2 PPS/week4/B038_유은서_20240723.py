def lengthofsnake(length, fruits):
    fruits.sort() 
    for fruit in fruits:
        if length >= fruit:  
            length += 1 
        else:
            break 
    return length

n, length = map(int, input().split())  
fruits = list(map(int, input().split())) 

print(lengthofsnake(length, fruits))
