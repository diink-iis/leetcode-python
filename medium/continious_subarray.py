from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        divisions = {0: -1}
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            sum_nums %= k
            if sum_nums not in divisions:
                divisions[sum_nums] = i
            elif i - divisions[sum_nums] >= 2:
                return True
        return False