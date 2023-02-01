class Solution:
    def intervalIntersection(self, A, B) -> List[List[int]]:
        i = 0
        j = 0
         
        result = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            
            if a_start <= b_end and b_start <= a_end:                       
                # Criss-cross lock
                result.append([max(a_start, b_start), min(a_end, b_end)])   
                # Squeezing     
            if a_end <= b_end:         
                # Exhausted this range in A
                i += 1               
                # Point to next range in A
            else:                      
                # Exhausted this range in B
                j += 1               
                # Point to next range in B
        return result