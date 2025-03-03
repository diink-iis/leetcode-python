class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_cnt = {}

        for i in s:
            dict_cnt[i] = dict_cnt.get(i, 0) + 1

        for i in range(len(s)):
            if dict_cnt[s[i]] == 1:
                return i

        return -1
