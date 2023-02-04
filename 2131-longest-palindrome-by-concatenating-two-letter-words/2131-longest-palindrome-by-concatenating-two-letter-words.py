class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        C = Counter()
        ans = 0
        countrev = 0
        for word in words:
            rev_word = word[::-1]

            if rev_word in C and C[rev_word] > 0:

                if rev_word == word:
                    countrev -=1
                ans += 4
                C[rev_word] -= 1    
            else:
                if rev_word == word:
                    countrev += 1
                C[word] += 1

        return ans + 2 if countrev > 0 else ans