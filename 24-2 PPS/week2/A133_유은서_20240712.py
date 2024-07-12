# problem url: https://leetcode.com/problems/capitalize-the-title/
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ls = title.split(" ")
        a = []
        for i in ls:
            if len(i)==1 or len(i)==2: a.append(i.lower())
            else: a.append(i.capitalize())
        b= ' '.join([str(elem) for elem in a])
        return b