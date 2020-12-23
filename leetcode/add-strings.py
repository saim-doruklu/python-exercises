class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1AsList = list(num1)
        num2AsList = list(num2)
        num1Len = num1AsList.__len__()
        num2Len = num2AsList.__len__()

        carryOver = 0
        for index in range(max(num1Len, num2Len)):
            firstDigit = num1AsList[num1Len-1-index] if index < num1Len else 0
            secondDigit = num2AsList[num2Len-1-index] if index < num2Len else 0
            sum = int(firstDigit) + int(secondDigit) + carryOver
            carryOver = sum // 10
            sum = sum % 10
            if num1Len > num2Len:
                num1AsList[num1Len-1-index] = str(sum)
            else:
                num2AsList[num2Len-1-index] = str(sum)

        firstChar = str(carryOver) if carryOver > 0 else ""

        if num1Len > num2Len:
            return "".join([firstChar]+num1AsList)
        else:
            return "".join([firstChar]+num2AsList)

if __name__ == '__main__':
    sol = Solution()
    print(sol.addStrings("0","0"))