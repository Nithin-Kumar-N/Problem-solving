from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Use dynamic programming to determine if each substring of s can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True

        # Use backtracking to construct all possible sentences from the segmented substrings
        def backtrack(start):
            if start == len(s):
                return ['']
            sentences = []
            for end in range(start + 1, len(s) + 1):
                if dp[end]:
                    word = s[start:end]
                    if word in wordDict:
                        for sentence in backtrack(end):
                            if sentence:
                                sentences.append(word + ' ' + sentence)
                            else:
                                sentences.append(word)
            return sentences

        return backtrack(0)

# Example usage:
solution = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
result = solution.wordBreak(s, wordDict)
print(result)
