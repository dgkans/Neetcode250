class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 #top means top row and bottom means bottom row
        bottom = len(matrix)-1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] >= target:
                bottom = mid - 1
            else:
                top = mid + 1
        target_row = (top + bottom) // 2
        left = 0
        right = len(matrix[target_row])-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
