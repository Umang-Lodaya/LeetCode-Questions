#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        freq = [0 for _ in range(26)]
        
        start = 0; end = 0; n = len(s)
        ans = -1; unique = 0
        
        while end < n:
            if freq[ord(s[end]) - ord('a')] == 0:
                unique += 1
            
            freq[ord(s[end]) - ord('a')] += 1
            
            while unique > k:
                if freq[ord(s[start]) - ord('a')] == 1:
                    unique -= 1
                
                freq[ord(s[start]) - ord('a')] -= 1
                start += 1
            
            if unique == k:
                ans = max(ans, end - start + 1)
            
            end += 1
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends