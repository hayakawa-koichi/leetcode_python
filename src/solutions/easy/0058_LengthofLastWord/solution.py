"""
ある単語をある数の空白で区切った文字列 s が与えられたとき、その文字列の最後の単語の長さを返す。
単語は、非空白文字のみからなる最大部分文字列である。

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        word = ''

        for i, e in enumerate(s):
            if e != " ":
                word += e
                # end of str
                if i == len(s) - 1:
                    words.append(word)
                    break
            elif word:
                words.append(word)
                word = ''
            else:
                pass

        return len(words[len(words)-1])


s = Solution()
s.lengthOfLastWord("   fly me   to   the moon  ")
