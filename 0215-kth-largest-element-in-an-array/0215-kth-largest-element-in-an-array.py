class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(arr, k):
            pivot = random.choice(arr)
            left, mid, right = [], [], []
            
            for a in arr:
                if a > pivot:
                    left.append(a)
                elif a < pivot:
                    right.append(a)
                else:
                    mid.append(a)
            
            if len(left) >= k:
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)