class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        if s == goal:
            count = [0] * 26

            for i in range(len(s)):
                c = ord(s[i]) - ord('a')
                count[c] += 1
                if count[c] == 2:
                    return True

            return False

        index1 = -1
        index2 = -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if index1 == -1:
                    index1 = i
                elif index2 == -1:
                    index2 = i
                else:
                    return False

        if index2 == -1:
            return False

        return s[index1] == goal[index2] and s[index2] == goal[index1]