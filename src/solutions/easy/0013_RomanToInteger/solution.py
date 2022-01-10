class Solution:
    """
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    ex)
        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    IをV（5）とX（10）の前に置くと、4と9になります。
    XはL(50)とC(100)の前に置くと40と90になる。
    CはD(500)とM(1000)の前に置くと、400と900になる。
    """
    def mySolution(self, s: str) -> int:

        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        two_roman_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        ans = 0

        for i, e in enumerate(s):
            if 0 < i and s[i-1]+s[i] in two_roman_dict:
                continue
            if i+1 < len(s) and e+s[i+1] in two_roman_dict:
                ans += two_roman_dict[e+s[i+1]]
            else:
                ans += roman_dict[e]

        return ans

    def mostVotesSolution(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

s = Solution()
s.mostVotesSolution("MCMXCIV")
