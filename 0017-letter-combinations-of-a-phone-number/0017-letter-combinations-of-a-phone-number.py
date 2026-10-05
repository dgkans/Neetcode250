from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # No digits means no combinations
        if digits == "":
            return []

        # Letters available for each digit
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        n = len(digits)

        def generate(index, curr):
            # One letter has been chosen for every digit
            if index == n:
                res.append(curr)
                return

            # Read the letters for the current digit
            digit = digits[index]
            letters = mapping[digit]

            # Choose each letter and process the next digit
            for letter in letters:
                generate(index + 1, curr + letter)

        # Begin at the first digit with an empty string
        generate(0, "")
        return res