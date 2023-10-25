#User function Template for python3

class Solution:
    def knapSack(self, num_items, max_weight, values, weights):
        dp_table = [0] * (max_weight + 1)

        for weight_capacity in range(1, max_weight + 1):
            for item_index in range(num_items):
                if weights[item_index] <= weight_capacity:
                    included_value = dp_table[weight_capacity - weights[item_index]] + values[item_index]
                    dp_table[weight_capacity] = max(dp_table[weight_capacity], included_value)


        return dp_table[max_weight]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends