class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result = []
        allProducts = []

        for index, c in enumerate(reversed(num1)):
            thisProduct = ["0"] * int(index)
            carryOver = 0
            for index2, c2 in enumerate(reversed(num2)):
                multiplicationOfSingleDigits = (int(c) * int(c2)) + carryOver
                carryOver = multiplicationOfSingleDigits // 10
                thisDigit = multiplicationOfSingleDigits % 10
                thisProduct.append(str(thisDigit))
            if carryOver > 0:
                thisProduct.append(str(carryOver))
            allProducts.append(thisProduct)
        maxProductLength = (allProducts[allProducts.__len__() - 1]).__len__()

        carryOver = 0
        for zeroToMaxProductLength in range(1, maxProductLength + 1):
            sum = 0
            for product in allProducts:
                if product.__len__() >= zeroToMaxProductLength:
                    sum = sum + int(product[zeroToMaxProductLength-1])
            sum = sum + carryOver
            carryOver = sum // 10
            result.append(str(sum % 10))
        if carryOver > 0:
            result.append(str(carryOver))

        return str.join("", reversed(result))

if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply("0", "456"))