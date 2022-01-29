"""
非負の整数xが与えられたとき、xの平方根を計算し、返す。
戻り値の型が整数であるため、10進数は切り捨てられ、結果の整数部のみが返されます。
注:pow(x, 0.5) や x ** 0.5 などの組み込み指数関数や演算子を使用することはできません。

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1
        while s <= x:
            if s * s > x:
                break
            s += 1
        return s - 1


s = Solution()
print(s.mySqrt(1))
