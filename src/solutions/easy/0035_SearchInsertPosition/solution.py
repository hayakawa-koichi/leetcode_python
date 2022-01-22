"""
異なる整数のソートされた配列と目標値が与えられたとき、目標が見つかればそのインデックスを返す。
見つからない場合は、順番に挿入された場合のインデックスを返す。
実行時の計算量が O(log n) であるアルゴリズムを書くこと．

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

s = Solution()
print(s.searchInsert(nums=[1,3,5,6], target=5))
