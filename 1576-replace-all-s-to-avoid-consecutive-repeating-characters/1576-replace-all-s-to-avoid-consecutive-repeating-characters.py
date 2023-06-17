class Solution:
    def modifyString(self, s: str) -> str:
        s = list("#" + s + "#")
        
        for i in range(1, len(s) - 1):
            if s[i] == "?":
                while True:
                    char = random.choice(string.ascii_lowercase)
                    if char not in [s[i-1], s[i+1]]:
                        s[i] = char
                        break

        return "".join(s[1:-1])