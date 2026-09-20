from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Maps each fruit type to its count in the current window
        basket = {}

        # Starting tree of the current window
        left = 0

        # Largest valid number of fruits found
        longest = 0

        for right in range(len(fruits)):
            # Add the fruit from the new rightmost tree
            fruit = fruits[right]

            if fruit in basket:
                basket[fruit] += 1
            else:
                basket[fruit] = 1

            # Three types cannot fit into two baskets
            while len(basket) > 2:
                left_fruit = fruits[left]

                # Remove one fruit from the left side
                basket[left_fruit] -= 1

                # Remove the type only when none remain
                if basket[left_fruit] == 0:
                    del basket[left_fruit]

                # Move the window's starting position forward
                left += 1

            # The window now contains at most two types
            length = right - left + 1
            longest = max(longest, length)

        return longest