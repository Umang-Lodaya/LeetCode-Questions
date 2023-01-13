class Solution:
    def isPalindrome(self, x: int) -> bool:
        char = str(x)
        return char == char[::-1]