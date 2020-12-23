import re

class Solution:
    def myAtoi(self, s: str) -> int:
        intMax = (2**31)-1
        intMin = -2**31
        p = re.compile('^\s*(?P<actualNumber>[+-]?\d+)')
        for m in p.finditer(s):
            resultStr = m.group().strip()
            if resultStr.__len__() == 0:
                return 0
            resultInt = int(resultStr)
            if resultInt > intMax:
                return intMax
            elif resultInt < intMin:
                return intMin
            else:
                return resultInt
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi("+-12"))