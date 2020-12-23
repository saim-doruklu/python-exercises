import re


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        intRegex = re.compile('^[+-]?\d+$')
        floatingOne = re.compile('^[+-]?(\d+)(|\.(|\d+))$')
        floatingTwo = re.compile('^[+-]?(|\d+)\.(\d+)$')
        exponentialOne = re.compile('^[+-]?(|\d+)\.(\d+)e[+-]?(0|([1-9]\d*))\d*$')
        exponentialTwo = re.compile('^[+-]?(\d+)(|\.(|\d+))e[+-]?(0|([1-9]\d*))\d*$')
        if intRegex.match(s) or floatingOne.match(s) or floatingTwo.match(s) or exponentialOne.match(s) or exponentialTwo.match(s):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isNumber("0"), "true")
    print(sol.isNumber(" 0.1 "), "true")
    print(sol.isNumber("abc"), "false")
    print(sol.isNumber("1 a"), "false")
    print(sol.isNumber("2e10"), "true")
    print(sol.isNumber(" -90e3   "), "true")
    print(sol.isNumber(" 1e"), "false")
    print(sol.isNumber("e3"), "false")
    print(sol.isNumber(" 6e-1"), "true")
    print(sol.isNumber(" 99e2.5 "), "false")
    print(sol.isNumber("53.5e93"), "true")
    print(sol.isNumber(" --6 "), "false")
    print(sol.isNumber("-+3"), "false")
    print(sol.isNumber("95a54e53"), "false")
    print(sol.isNumber(".1"), "true")
    print(sol.isNumber("e9"), "false")
    print(sol.isNumber(".2e9"), "true")
    print(sol.isNumber("2.e9"), "true")
    print(sol.isNumber("3."), "true")
    print(sol.isNumber("."), "False")
    print(sol.isNumber(".e9"), "False")
    print(sol.isNumber("2e0"), "true")
    print(sol.isNumber("01."), "true")
    print(sol.isNumber(" "), "False")