"""
strStr()を実装する。
haystack に最初に出現する needle のインデックス、または needle が haystack の一部でない場合は -1 を返す。

明確化する。
needleが空文字列の場合、何を返せばよいのでしょうか？これは面接の時に聞いてみたい質問です。
この問題の趣旨から、needleが空文字列の場合は0を返すことにします。これはC言語のstrstr()やJavaのindexOf()と一致します。

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "":
            return 0

        return len(haystack.split(needle)[0]) if haystack.count(needle) else -1

s = Solution()
print(s.strStr(haystack="hello", needle="ll"))
