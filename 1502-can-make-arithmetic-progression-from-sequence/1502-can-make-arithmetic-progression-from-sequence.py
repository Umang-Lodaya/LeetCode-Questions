class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        cd = arr[1] - arr[0]
        
        for num in range(1, len(arr)-1):
            diff = arr[num+1] - arr[num]
            if (diff != cd):
                return False
        
        return True