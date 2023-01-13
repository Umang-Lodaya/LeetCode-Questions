class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = list(map(str, digits))
        d = ''.join(d)
        d = int(d) + 1
        d = str(d)
        return list(map(int, d))