"""
降順でない整数の配列 nums が与えられたとき、各要素が一度だけ現れるように、 重複をその場で削除せよ。要素の相対的な順序は同じでなければならない。
言語によっては配列の長さを変更することができないので、代わりに結果を配列numsの最初の部分に配置させる必要があります。
より正式には、重複を取り除いた後にk個の要素がある場合、numsの最初のk個の要素に最終的な結果を格納しなければなりません。最初のk個の要素から先は何を残してもかまいません。
最終結果をnumsの最初のk個のスロットに配置した後、kを返す。
別の配列のために余分な領域を確保しないでください。O(1) 個のメモリを追加して，入力配列をインプレースで変更しなければなりません．

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        isIncludeUnderscore = False
        for i in range(len(nums)-1):
            while nums[i] == nums[i+1]:
                del nums[i]
                nums.append('_')
                isIncludeUnderscore = True
                if nums[i] == nums[i] == '_':
                    break

        return nums.index('_') if isIncludeUnderscore else len(nums)


s = Solution()
s.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4])
