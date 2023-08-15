#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        ones = 0
        for i in a:
            if i == 1:
                ones += 1
        
        zeros = 0; maxZeros = 0
        for i in a:
            if i == 0:
                zeros += 1
            elif zeros:
                zeros -= 1
            maxZeros = max(maxZeros, zeros)
        
        return ones + maxZeros


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends