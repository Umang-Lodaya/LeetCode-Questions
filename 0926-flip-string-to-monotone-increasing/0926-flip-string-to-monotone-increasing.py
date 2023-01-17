class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroes, ones = s.count('0'), 0
        output = zeroes
        
        for char in s:
            if char == '0':
                zeroes -= 1
            else:
                ones += 1
            
            output = min(output, zeroes+ones)
        return output