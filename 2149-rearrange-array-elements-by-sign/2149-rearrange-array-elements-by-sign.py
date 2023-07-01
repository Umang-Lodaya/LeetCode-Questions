class Solution:
    def rearrangeArray(self, arr):
        # code here
        p = [i for i in arr if i >= 0]
        n = [i for i in arr if i < 0]
        
        i=0; j=0; k=0
        while i < len(p) and j < len(n):
            if k % 2 == 0:
                arr[k] = p[i]
                k += 1
                i += 1
            else:
                arr[k] = n[j]
                k += 1
                j += 1
        
        while i < len(p):
            arr[k] = p[i]
            k += 1
            i += 1
        
        while j < len(n):
            arr[k] = n[j]
            k += 1
            j += 1
        
        return arr