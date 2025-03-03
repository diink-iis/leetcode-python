from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sorted_ranges = []
        if not nums:
            return sorted_ranges

        init = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                if init == nums[i - 1]:
                    sorted_ranges.append(str(init))
                else:
                    sorted_ranges.append(f"{init}->{nums[i - 1]}")
                if i < len(nums):
                    init = nums[i]
        return sorted_ranges




