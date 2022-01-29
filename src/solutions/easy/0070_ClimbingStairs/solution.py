"""
あなたは階段を登っています。頂上まで行くにはn段の階段が必要です。
1回ごとに1段か2段のどちらかを登ることができる。この場合、頂上までの登り方はいくつに分かれますか？

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

import math


class Solution:

    def __giveup(self, n: int) -> int:
        if n in (1,2):
            return n
        def __comb(n, r):
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
        ans = 1
        i = 1


        while n-i > n//2:
            ans+=__comb(n-i,1)
            i+=1
        return ans


    # example
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a


s = Solution()
print(s.climbStairs(5))
