# problem url: https://www.acmicpc.net/problem/4659
import sys
input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u'}  # Set로 변경하여 in 연산 최적화

while True:
    password = input().rstrip()
    if password == 'end':
        break
    
    has_vowel = any(char in vowels for char in password)
    is_acceptable = True
    last_char = ""
    vowel_count = 0
    consonant_count = 0
    
    for i, char in enumerate(password):
        if i > 0 and char == last_char and char not in {'e', 'o'}:
            is_acceptable = False
            break
        
        if char in vowels:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        
        if vowel_count == 3 or consonant_count == 3:
            is_acceptable = False
            break
        
        last_char = char

    if has_vowel and is_acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
