#User function Template for python3

class Solution:
    def reverseWord(self, s):
        s = list(s)
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        
        return ''.join(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends