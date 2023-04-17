class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [None]*len(candies)
        
        for i in range(len(candies)):
            new = candies[i] + extraCandies
            result[i] = new >= max(candies)
        
        return result