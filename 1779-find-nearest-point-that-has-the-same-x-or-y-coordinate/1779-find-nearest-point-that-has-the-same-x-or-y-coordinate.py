class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx = -1
        smallest = float("inf")
        for p in points:
            if p[0] == x or p[1] == y:
                dist = abs(x - p[0]) + abs(y - p[1])
                if dist < smallest:
                    idx = points.index(p)
                    smallest = dist
                # elif dist == smallest:
                #     if points.index(p) < idx:
                #         idx = points.index(p)
                #         smallest = dist
        return idx