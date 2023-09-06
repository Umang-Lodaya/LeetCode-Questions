class Solution:
    def duplicates(self, arr, n):
        mp = dict()
        l = []
        for i in range(n):
            if arr[i] in mp.keys():
                mp[arr[i]] += 1
            else:
                mp[arr[i]] = 1
                
        for x in mp:
            if mp[x] != 1:
                l.append(x)
                
        if len(l) == 0 :
            return [-1]
        
        l.sort()
        return l
    	        
    	    
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends