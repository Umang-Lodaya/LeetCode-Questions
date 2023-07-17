#User function Template for python3
from collections import OrderedDict

class Solution:
    def FirstNonRepeating(self, A):
        count_dict = OrderedDict()
        result = []
        
        for ch in A:
            count_dict[ch] = count_dict.get(ch, 0) + 1
            
            non_repeating_ch = None
            for key, value in count_dict.items():
                if value == 1:
                    non_repeating_ch = key
                    break
            
            if non_repeating_ch:
                result.append(non_repeating_ch)
            else:
                result.append('#')
        
        return ''.join(result)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends