"""
整数配列numsと整数valが与えられたとき、nums内のvalの出現をすべてインプレースで削除します。要素の相対的な順序は変更可能である。
言語によっては配列の長さを変更することができないので、代わりに結果を配列numsの最初の部分に配置させなければならない。
より正式には、重複を取り除いた後にk個の要素がある場合、numsの最初のk個の要素に最終的な結果を格納しなければなりません。最初のk個の要素から先は何を残してもかまいません。
最終結果をnumsの最初のk個のスロットに配置した後、kを返す。
別の配列のために余分な領域を確保しないでください。O(1) 個のメモリを追加して，入力配列をインプレースで変更しなければなりません．

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

from typing import List

class Solution:
    def myanswer__giveup(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        if cnt == 0:
            return 0

        for i in range(len(nums)):
            if nums[i] == val:
                del nums[i]
                nums.append('_')
        return len(nums) - cnt

    def mostVotedAnswer(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1

        return i

s = Solution()
s.mostVotedAnswer(
    nums=[0,1,2,2,3,0,4,2],
    val=2
)
