class Solution:
    def reverseWords(self, s: str) -> str:
        spaces_removed = s.strip()
        words = spaces_removed.split()
        words.reverse()#can use st[::-1] which returns a new list unlike inplace reversal of rev()
        result = " ".join(words)
        return result
