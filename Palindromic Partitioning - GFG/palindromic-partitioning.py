#User function Template for python3

class Solution:
    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
            
        return True
        
    def palindromicPartition(self, string):
        length = len(string)
        min_cuts = [0 for _ in range(length)]
        
        for i in range(length):
            min_cut = i
            for j in range(i, -1, -1):
                if self.isPalindrome(string, j, i):
                    min_cut = 0 if j == 0 else min(min_cut, 1 + min_cuts[j - 1])
                
            min_cuts[i] = min_cut
        
        return min_cuts[length - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends