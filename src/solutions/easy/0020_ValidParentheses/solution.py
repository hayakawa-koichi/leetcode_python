"""
文字 '(', ')', '{', '}', '[', ']' のみを含む文字列 s が与えられたとき、その入力文字列が有効かどうかを判定する。

入力文字列が有効であるのは、以下の場合である。

1. 開き括弧は、同じ種類の括弧で閉じなければならない。
2. 開いている括弧は正しい順序で閉じなければならない。

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""
class Solution:
    def isValid(self, s: str) -> bool:

        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for char in s:
            if char in pair.values():
                stack.append(char)
            elif char in pair.keys():
                # popは指定なしの場合リストの最後の要素を削除し、
                # その要素の値を取得できる。
                if stack == [] or pair[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []

s = Solution()
# s.isValid("{[]}")
s.isValid("([)]")
