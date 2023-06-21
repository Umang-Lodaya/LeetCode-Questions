class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = address.split('.')
        return "[.]".join(arr)