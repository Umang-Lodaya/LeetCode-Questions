class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # prefix sums encountered in current path
        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                # Can remove sums[currSum-targetSum] prefixSums to get target
                count = sums[total-targetSum]

                # Add value of this prefixSum
                sums[total] += 1
                # Explore children
                count += dfs(root.left, total) + dfs(root.right, total)
                # Remove value of this prefixSum (path's been explored)
                sums[total] -= 1

            return count

        return dfs(root, 0)