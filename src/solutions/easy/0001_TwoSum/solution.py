from typing import List

class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    # my first answer
    def mySolution(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    break
                if num1 + num2 == target:
                    return [i,j]

    # Hereafter, model answers
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(i, j)
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        簡単な実装では、2回の反復を行う。
        最初の反復では、各要素の値をキーとして、そのインデックスを値としてハッシュテーブルに追加する。
        次に、2回目の反復で、各要素の補数（target - nums[i]target-nums[i] ）がハッシュテーブルに存在するかどうかをチェックする。
        存在する場合は、現在の要素のインデックスとその補集合のインデックスを返す。補集合はnums[i]nums[i]そのものであってはならないことに注意!
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """
        イテレートしてハッシュテーブルに要素を挿入している間に、現在の要素の補数がすでにハッシュテーブルに存在するかどうかをチェックするために振り返る。
        もし存在すれば、解決策が見つかったことになり、すぐにそのインデックスを返します。
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            print(hashmap)
            print(complement)
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

# s = Solution()
# s.twoSum3(nums=[2,7,11,15], target=26)
