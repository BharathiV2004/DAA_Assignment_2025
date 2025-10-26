from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Finds the smallest path sum from top to bottom in a triangle.
        #We start from the bottom and work our way up, updating the minimum sums along the way.
        if not triangle:
            # If the triangle is empty, there’s nothing to sum
            return 0
        # Make a copy of the last row. Think of this as our "running totals".
        running_totals = triangle[-1].copy()
        # Go from the second-to-last row up to the top
        for row_index in range(len(triangle) - 2, -1, -1):
            for col_index in range(len(triangle[row_index])):
                # For each number, pick the smaller path from the two numbers below it
                running_totals[col_index] = (
                    triangle[row_index][col_index] 
                    + min(running_totals[col_index], running_totals[col_index + 1])
                )
        # By the time we reach the top, the first element has the minimum path sum
        return running_totals[0]
