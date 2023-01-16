class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        while(n>1):
            if(n%3!=0):
                return False
            n /= 3
        
        if(n==1):
            return True
            
        return False