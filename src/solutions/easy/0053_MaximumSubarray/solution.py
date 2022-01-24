"""
整数配列numsが与えられたとき、
最大の和を持つ連続した部分配列（少なくとも1つの数を含む）を見つけ、その和を返す。
サブアレイとは、配列の連続した部分のことです。

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""



from typing import List


class Solution:
    def __giveup(self, nums: List[int]) -> int:
        pass
        # def __sort_asc(subarray: List[int], nums: List[int]):

        #     subarray = nums
        #     for i in range(len(nums)):
        #         if sum(subarray) <= sum(nums[i:]):
        #             subarray = nums[i:]
        #             print(subarray)
        #     return subarray

        # def __sort_desc(subarray: List[int], nums: List[int]):
        #     print(nums)
        #     if len(nums) == 1:
        #         return nums

        #     subarray = nums
        #     for i in range(len(nums)):
        #         if sum(subarray) <= sum(nums[:i]):
        #             subarray = subarray[:i]
        #     return subarray

        # if len(nums) == 1:
        #     return sum(nums)
        # h = __sort_asc([], nums)
        # i = __sort_desc([], h)
        # print(i)
        # return sum(i)

    def solution(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                print(nums[i])
                nums[i] += nums[i-1]
        print(max(nums))
        return max(nums)

s = Solution()
s.solution([-2,1,-3,4,-1,2,1,-5,4])
