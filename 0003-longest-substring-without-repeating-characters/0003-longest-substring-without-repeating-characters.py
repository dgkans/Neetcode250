class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        sub_len = 0
        for right in range(len(s)):
            while s[right] in window:
                window.discard(s[left])
                left+=1
            window.add(s[right])
            sub_len = max(right-left+1,sub_len)
        return sub_len
                

