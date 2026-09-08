from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        #check for fail condition with too many repeating chars
        if max(freq.values()) > (n + 1) // 2:
            return ""
        prev_char = ''
        result = []
        for i in range(n):
            top = freq.most_common(2)
            if top[0][0] != prev_char:
                best_char = top[0][0]
            else:
                best_char = top[1][0]
            result.append(best_char)
            freq[best_char]-=1

            if freq[best_char]==0:
                del freq[best_char]
            
            prev_char = best_char
        return ''.join(result)
            