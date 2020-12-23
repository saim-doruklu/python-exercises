class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = a.__len__()
        lenB = b.__len__()
        carryOver = 0
        result = []
        for index in range(0, max(lenA,lenB)):
            digitFromA = int(a[lenA-1-index]) if index < lenA else 0
            digitFromB = int(b[lenB - 1 - index]) if index < lenB else 0
            sum = digitFromA + digitFromB + carryOver
            thisDigit = sum % 2
            carryOver = sum // 2
            result.append(str(thisDigit))
        if carryOver > 0:
            result.append(str(carryOver))
        return "".join(reversed(result))

if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11","1"))