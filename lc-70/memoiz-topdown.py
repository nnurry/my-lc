class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic programming problem:
        - Subproblem: After climbed x-step, how many ways to climb n-x steps
        """
        memo = {
            1: 1,
            2: 2,
            3: 3,
        }

        def helper(n):
            # Closure for memo passing
            if n == 0:
                return 1
            if n < 0:
                return 0

            if n in memo:
                print(f"Retrieve {n} from memo: {memo[n]}")
                return memo[n]                

            climb_by_1 = helper(n-1)
            climb_by_2 = helper(n-2)

            climbs = climb_by_1 + climb_by_2

            memo[n-1] = climb_by_1
            memo[n-2] = climb_by_2
            return climbs

        return helper(n)

import sys

print(Solution().climbStairs(int(sys.argv[1])))