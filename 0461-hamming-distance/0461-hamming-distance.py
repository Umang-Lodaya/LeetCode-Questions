class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        
        if len(x_bin) > len(y_bin):
            while len(y_bin) != len(x_bin):
                y_bin = "0" + y_bin
        else:
            while len(y_bin) != len(x_bin):
                x_bin = "0" + x_bin
        
        # print([x_bin, y_bin], sep='\n')
        
        count = 0
        for i, j in zip(x_bin, y_bin):
            if i != j: count += 1
        
        return count