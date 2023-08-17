#User function Template for python3
class Solution:

    def generateNextPalindrome(self,num, n ) :
        flag = False
        mid = (n-1)//2
        
        for i in range(mid + 1, n) :
            if num[i] == num[n-i-1] : continue
            if num[i] < num[n-i-1] :
                flag = True
                break
            else:
                break
            
        if flag:
            for i in range(mid + 1, n):
                num[i] = num[n-i-1]
                
            res = num.copy()
            return res
            
        index = -1
        for i in range(mid, -1, -1):
            if(num[i] < 9):
                index = i
                break
            
        if(index == -1):
            flag1 = False
            for i in range(mid + 1, n):
                if(num[i] != 9) :
                    flag1 = True
                    break
                
            if flag1:
                res = [9] * n
                return res
            
            res = [0] * (n + 1)
            res[0] = 1
            res[n] = 1
            return res
            
        num[index] += 1
        
        for i in range(index + 1, mid + 1):
            num[i] = 0
        
        for i in range(mid + 1, n) : 
            num[i] = num[n - i - 1]
            
        res = num.copy()
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends