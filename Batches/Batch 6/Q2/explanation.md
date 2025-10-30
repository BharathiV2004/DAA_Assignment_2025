**Problem Link:**

[LeetCode - Word Break II](https://leetcode.com/problems/word-break-ii/description/)

**Problem Statement:**

Given a string s and a dictionary of words wordDict, return all possible sentences where s can be segmented into space-separated words from the dictionary.
Each word in the dictionary may be used multiple times.

**Sample:**

**Input:**

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]


**Output:**

["cats and dog", "cat sand dog"]


**Explanation:**
Two possible ways to split the string into valid words:

"cats and dog"

"cat sand dog"

**Algorithm / Approach:**

1.We solve this using DFS + Memoization (backtracking): Convert wordDict into a set for O(1) lookups.

2.Define a recursive function dfs(start) that returns all valid sentences formed from s[start:].

3.For each possible end index end > start:
   
   If s[start:end] is in the word set: 
  
- Recursively get all sentences from dfs(end) (the rest of the string).
- Prepend s[start:end] to each sentence from the recursion (with a space if needed).
- Use a memo dictionary to store results for each start index to avoid recomputation.
- Return the list of sentences for dfs(0) — the full string.

**Why this works:**

DFS explores all possible segmentations, and memoization ensures we do not recompute results for the same substring multiple times, which drastically improves efficiency.

**Time Complexity:**

- Time Complexity: Exponential in the worst case (number of possible sentences). Memoization reduces repeated work.
  
               -Best Case: O(n²) — only one valid segmentation path; each substring checked once, and memoization prevents recomputation.
                -Average Case: O(n² × k) — some branching occurs (k valid next words on average), but memoization reduces redundant DFS calls.
                -Worst Case: O(2ⁿ) — every substring is valid (e.g., "aaaaa" type case), causing exponential branching and many possible sentence combinations.


**Space Complexity:**

- Space Complexity: O(n * L) for recursion stack and memo storage (n = length of string, L = average length of sentence). Output space can also be exponential.

**Example Input / Output:**

**Input:**

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

**Output:**

['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']

**Explanation:**

The string "pineapplepenapple" can be split into dictionary words in three ways:

"pine apple pen apple"

"pineapple pen apple"

"pine applepen apple"

Each segment in every sentence is a valid word from the dictionary. DFS explores all splits, and memoization avoids repeated work.
