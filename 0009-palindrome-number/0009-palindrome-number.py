class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
             rev_num = int(str(x)[::-1])
        return rev_num == x