from math import gcd
from typing import List

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d[0], d[1]
        r1, r2 = r[0], r[1]
        
        # LCM: hours where BOTH drones recharge simultaneously
        L = r1 * r2 // gcd(r1, r2)
    
        def canFinish(T: int) -> bool:
            Hn = T // L
            H1_only = T // r2 - Hn
            H2_only = T // r1 - Hn
            Hb = T - T // r1 - T // r2 + Hn
            
            if d1 > H1_only + Hb:
                return False
            if d2 > H2_only + Hb:
                return False
            if d1 + d2 > H1_only + H2_only + Hb:
                return False
            return True
        
        # Binary search on the answer
        lo = 1
        hi = 2 * (d1 + d2) * max(r1, r2)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo