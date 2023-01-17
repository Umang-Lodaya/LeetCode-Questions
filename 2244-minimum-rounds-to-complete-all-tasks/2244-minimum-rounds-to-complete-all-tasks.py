from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        d, count = Counter(tasks), 0
        
        for i in d.values():
            if i == 1:
                return -1
            count += (i+2)//3

        return count
        