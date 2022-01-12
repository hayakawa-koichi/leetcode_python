from typing import List, Optional
import itertools

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
2つのソート付きリンクリスト list1 と list2 の先頭が与えられる。
この2つのリストを1つのソートされたリストに統合しなさい。リストは最初の2つのリストのノードをつなぎ合わせたものでなければなりません。
マージされたリンクリストの先頭を返せ。

ex
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""
class Solution:
    def myanswer__giveup(self, list1: Optional[List], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = list(itertools.chain.from_iterable([list1, list2]))
        mergedList.sort()
        return mergedList


    def mostVotedSolution(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

s = Solution()
s.myanswer__giveup(list1=[1,2,4], list2=[1,3,4])
