from collections import Counter

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = Counter()
        if a > 0:
            freq['a'] = a
        if b > 0:
            freq['b'] = b
        if c > 0:
            freq['c'] = c
        
        result = []
        
        while freq:
            # Get top 2 most frequent characters
            top = freq.most_common(2)
            
            # Would picking the top char create a triple?
            makes_triple = (len(result) >= 2
                            and result[-1] == top[0][0]
                            and result[-2] == top[0][0])
            
            # Pick the first one unless it would make a triple
            if not makes_triple:
                best_char = top[0][0]
            elif len(top) > 1:
                best_char = top[1][0]
            else:
                break  # only one char left and it would make a triple
            
            result.append(best_char)
            freq[best_char] -= 1
            
            # Clean up: remove chars with count 0 so most_common stays clean
            if freq[best_char] == 0:
                del freq[best_char]
        
        return ''.join(result)