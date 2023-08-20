#User function Template for python3
class Solution:

	def count(self,arr, n, x):
	    
		def leftMostEle(arr, n, x):
		    l = 0; h = n - 1
		    inx = -1
		    while l <= h:
		        mid = l + (h - l) // 2
		        if arr[mid] == x:
		            inx = mid
		            h = mid - 1
		        elif arr[mid] > x:
		            h = mid - 1
		        else:
		            l = mid + 1
		    
		    return inx
	    
		def rightMostEle(arr, n, x):
		    l = 0; h = n - 1
		    inx = -1
		    while l <= h:
		        mid = l + (h - l) // 2
		        if arr[mid] == x:
		            inx = mid
		            l = mid + 1
		        elif arr[mid] > x:
		            h = mid - 1
		        else:
		            l = mid + 1
		    
		    return inx
		
		s = leftMostEle(arr, n, x)
		if s == -1:
		    return 0
		e = rightMostEle(arr, n, x)
		return e - s + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends