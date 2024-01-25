class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        s = list(word)
        start = end = 0
        n = len(word)
        while end < n and s[end] != ch:
            end += 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)      