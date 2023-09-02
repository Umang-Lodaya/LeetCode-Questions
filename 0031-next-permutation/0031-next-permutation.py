class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def nextP(arr):
            N = len(arr)
            ind = -1
            for i in range(N-2, -1, -1):
                last = arr[i+1]
                slast = arr[i]
                if slast < last:
                    ind = i
                    break
            
            if ind == -1:
                return arr.reverse()
            
            for i in range(N-1, ind, -1):
                if arr[ind] < arr[i]:
                    arr[ind], arr[i] = arr[i], arr[ind]
                    break
            
            arr[ind+1:] = reversed(arr[ind+1:])
            return arr
        
        nums = nextP(nums)