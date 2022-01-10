from typing import List


class Solution:
    """
    文字列の配列の中で、最も長い共通の接頭辞を持つ文字列を求める関数を作成しなさい。
    共通の接頭辞がない場合は、空文字列 "" を返す。
    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ''
        for s in zip(*strs):
            if len(set(s)) > 1:
                break
            commonPrefix += ''.join(list(set(s)))
        return commonPrefix


    def mostVotedSolution(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if not strs:
                return ""
            shortest = min(strs,key=len)
            for i, ch in enumerate(shortest):
                print(i, ch)
                for other in strs:
                    if other[i] != ch:
                        return shortest[:i]
            return shortest

# s = Solution()
# s.mostVotedSolution(strs=["flower","flow","flight"])
# s.longestCommonPrefix(strs=['aiueo','kakikukeko', 'sashisuseso'])
