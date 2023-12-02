class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = []
        for word in words:
            for char in word:
                if chars.count(char) < word.count(char):
                    break
            else:
                result.append(len(word))
                
        return sum(result)