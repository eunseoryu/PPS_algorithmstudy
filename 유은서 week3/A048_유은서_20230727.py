n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for idx in range(len(word) - 1):
        if word[idx] != word[idx+1]:
            other = word[idx+1:]
            if other.count(word[idx])> 0:
                error += 1
    if error == 0:
        group_word += 1

print(group_word)            