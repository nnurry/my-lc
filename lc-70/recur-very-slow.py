class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            climb_by_1 = self.climbStairs(n-1)
            climb_by_2 = self.climbStairs(n-2)

            climbs = climb_by_1 + climb_by_2

            return climbs

        return helper(n)
        