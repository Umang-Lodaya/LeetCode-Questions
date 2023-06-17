class Solution:
    def relativeSortArray(self, A, B):
        return sorted(A, key=(B + sorted(A)).index)