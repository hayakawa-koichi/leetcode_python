"""
整数配列digitで表される大きな整数が与えられ、各digit[i]は整数のi番目の桁を表す。
各桁は左から右へ最上位から最下位へと並べられている。大きな整数には先頭の0は含まれない。

大きな整数を1つ増やし、その結果の配列digitを返す。

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = sum([d*10**i for i, d in enumerate(reversed(digits))])
        s += 1
        return [e for e in str(s)]

s = Solution()
s.plusOne([4,3,2,1])
