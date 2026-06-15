class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        minus_1 = 1
        minus_2 = 1
        for i in range(2, n+1):
            curr = minus_1 + minus_2
            minus_2 = minus_1
            minus_1 = curr
        return minus_1
