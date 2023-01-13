class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join(list(map(str, num)))) + k
        return list(map(int, list(str(num))))