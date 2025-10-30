**Minimum Path Sum in a Triangle:**

**Problem Link:**

[LeetCode - Triangle](https://leetcode.com/problems/triangle/)

**Problem Statement:**

Given a triangle array, find the minimum path sum from top to bottom.  
At each step, you may move to adjacent numbers on the row below.

**Sample:**

**Input:**

2  
3 4  
6 5 7  
4 1 8 3 

**Output:**

The minimum path sum here is `11` (2 → 3 → 5 → 1).

**Algorithm / Approach:**

We solve this using a bottom-up dynamic programming approach:

1. Start from the last row:
   Copy the last row into a list called `running_totals`.  
   This list will keep track of the minimum path sums for each position as we move up.

2. Move upwards row by row:  
   For each number in the current row:
   - Add it to the smaller of the two numbers directly below in `running_totals`.
   - Update `running_totals` at that position with this new sum.

3. Repeat until you reach the top row: 
   After processing all rows, `running_totals[0]` contains the **minimum path sum from top to bottom.

**Why this works:**

Each element only depends on the two elements below it. By starting from the bottom, we always know the minimum sums of the paths below, so we can update efficiently without needing a full 2D DP table.

**Time Complexity:**
 
   Best Case: O(n²) — every element in the triangle is visited once (no early exits possible).

   Average Case: O(n²) — same as best; algorithm always processes all elements.

   Worst Case: O(n²) — still visits every element once; no case causes extra work.

**Space Complexity:**

- Space Complexity: O(n)  
  We only need a single list to store the running totals of the current row.

**Example Input / Output:**

**Input:**

triangle = [
    [1],
    [2, 3],
    [4, 5, 6]
]

**Output:**

7

**Explanation:** The minimum path is 1 → 2 → 4 = 7.
