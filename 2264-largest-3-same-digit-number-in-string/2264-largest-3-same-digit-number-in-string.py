class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = -1
        
        l = 0; r = 1

        while r < len(num):
            if num[l] != num[r]:
                l = r
                r += 1

            else:
                if r - l == 2:
                    max_num = max(max_num, int(num[l]))
                    l = r + 1
                    r = l + 1
                else:
                    r += 1
                    
        return "" if max_num == -1 else f"{max_num}" * 3  