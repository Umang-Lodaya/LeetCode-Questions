class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.strip().split(' ')
        ans = list(filter(lambda x: x.startswith(searchWord), s))
        
        if ans == []:
            return -1
        else:
            return s.index(ans[0]) + 1