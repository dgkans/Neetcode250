class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            reversed_n = reversed_n << 1
            last_bit = n & 1
            reversed_n = reversed_n | last_bit
            n = n>>1
        return reversed_n