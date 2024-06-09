class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic programming problem:
        - Subproblem: After climbed x-step, how many ways to climb n-x steps
        """
        memo = {
            0: 1,
            1: 1,
        }
        for i in range(2, n+1):
            # From 2 to n
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]


import sys

print(Solution().climbStairs(int(sys.argv[1])))