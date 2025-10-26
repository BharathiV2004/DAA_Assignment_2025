
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #Returns all possible sentences where the string `s` can be segmented into words from `wordDict`.
        # Convert the word list into a set for O(1) lookups
        word_set = set(wordDict)
        memo = {}  # start index -> list of sentences
        def dfs(start: int) -> List[str]:
            if start == len(s):
                # Reached the end of the string: return a list with an empty string
                return [""]
            if start in memo:
                # Return already computed results for this start index
                return memo[start]
            sentences = []
            # Try every possible end index
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get all sentences for the substring starting at `end`
                    for suffix in dfs(end):
                        if suffix:
                            # If there is more string after current word, add a space
                            sentences.append(word + " " + suffix)
                        else:
                            sentences.append(word)
            # Memoize the result for this start index
            memo[start] = sentences
            return sentences
        return dfs(0)
