#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        self.mapp = {'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}
        
        num = 0
        for i in range(len(S)):
            if i > 0 and (self.mapp[S[i]] > self.mapp[S[i-1]]):
                num -= self.mapp[S[i-1]]
                num += self.mapp[S[i]] - self.mapp[S[i-1]]
            else:
                num += self.mapp[S[i]]
        
        return num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends