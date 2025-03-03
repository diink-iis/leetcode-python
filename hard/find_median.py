from math import floor
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_list = sorted(nums1 + nums2)
        print(full_list)
        lenght = len(full_list)
        if lenght % 2 != 0:
            if lenght == 1:
                return float(full_list[0])
            else:
                return float(full_list[floor(lenght / 2)])
        else:
            lenght = lenght // 2
            return float((full_list[lenght - 1] + full_list[lenght]) / 2)