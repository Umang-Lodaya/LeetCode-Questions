#User function Template for python3

class Solution:
    #Complete this function
    def power(self, N, R):
        m = (10 ** 9) + 7
        ans = 1
        base = N % m
        while R > 0:
            if R % 2 != 0:
                ans = (ans * base) % m
            base = (base * base) % m
            R = R // 2
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends