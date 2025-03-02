class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r - length + 1)
            else:
                if seen[s[r]] < length:
                    output = max(output, r - length + 1)
                else:
                    length = seen[s[r]] + 1
            seen[s[r]] = r
        return output
