#User function Template for python3
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        n = len(A)
        rotate = D
        rotate = rotate % n
        
        l = A[:rotate]
        j = 0
        for i in range(rotate,n):
            A[i-rotate] = A[i]
        
        for i in range(n - rotate, n):
            A[i] = l[j]
            j += 1
            
        return A

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends