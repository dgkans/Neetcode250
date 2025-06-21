class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == pow(2, int(math.log2(n))):
            return 1

        low = pow(2, int(math.log2(n)))
        high = pow(2, int(math.log2(n)) + 1)

        d1 = n - low
        d2 = high - n

        return 1 + min(self.minOperations(d1), self.minOperations(d2))
