"""
2つのバイナリ文字列a、bが与えられたとき、その和をバイナリ文字列として返す。

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))).split('0b')[1]

s = Solution()
print(s.addBinary(a="1010", b="1011"))
