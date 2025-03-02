class Solution:
    def expand_around_center(s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longest_palindromic_substring(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            palindrome_odd = Solution.expand_around_center(s, i, i)
            palindrome_even = Solution.expand_around_center(s, i, i + 1)
            longest = max(longest, palindrome_odd, palindrome_even, key=len)
        return longest