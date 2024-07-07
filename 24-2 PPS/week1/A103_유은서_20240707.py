# solution url: https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]

        morse_map = {chr(i + 97): morse[i] for i in range(26)}
        
        def word_to_morse(word):
            return ''.join(morse_map[char] for char in word)
        unique_transformations = {word_to_morse(word) for word in words}
        
        return len(unique_transformations)