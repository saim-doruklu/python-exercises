#
# class Solution:
#     def parseBoolExpr(self, expression: str) -> bool:
#         while expression.__len__() > 1:
#             expression = expression.replace("!(t)", "f")
#             expression = expression.replace("!(f)", "t")
#
#             expression = expression.replace("&(t,f", "&(f")
#             expression = expression.replace("&(f,t", "&(f")
#             expression = expression.replace("&(t,t", "&(t")
#             expression = expression.replace("&(f,f", "&(f")
#
#             expression = expression.replace("|(t,f", "|(t")
#             expression = expression.replace("|(f,t", "|(t")
#             expression = expression.replace("|(t,t", "|(t")
#             expression = expression.replace("|(f,f", "|(f")
#
#             expression = expression.replace("&(f)", "f")
#             expression = expression.replace("&(t)", "t")
#
#             expression = expression.replace("|(f)", "f")
#             expression = expression.replace("|(t)", "t")
#         return expression == "t"

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        parenthesisTuples = self.findMatchingParentheses(expression)
        return self.parseRecursive(expression, 0, expression.__len__(), parenthesisTuples)

    def parseRecursive(self, expression:str, startIndex, endIndex, parenthesisTuples, operation=None):

        part = expression[startIndex: endIndex]

        firstExpressionValue = None
        nextParenthesis = None

        if part.startswith("t"):
            firstExpressionValue = True
        elif part.startswith("f"):
            firstExpressionValue = False
        elif part.startswith("!"):
            nextParenthesis = parenthesisTuples[startIndex + 1]
            firstExpressionValue = not self.parseRecursive(expression, startIndex + 2, nextParenthesis, parenthesisTuples)
        elif part.startswith("&") or part.startswith("|"):
            nextParenthesis = parenthesisTuples[startIndex + 1]
            firstExpressionValue = self.parseRecursive(expression, startIndex + 2, nextParenthesis, parenthesisTuples, part[0])

        if nextParenthesis is not None and endIndex == nextParenthesis + 1:
            return firstExpressionValue
        if part.__len__() == 1:
            return firstExpressionValue

        if firstExpressionValue is True and operation == "|":
            return firstExpressionValue
        if firstExpressionValue is False and operation == "&":
            return firstExpressionValue

        newStartIndex = None
        if nextParenthesis is None:
            newStartIndex = startIndex + 2
        else:
            newStartIndex = nextParenthesis + 2

        return self.parseRecursive(expression,newStartIndex,endIndex,parenthesisTuples,operation)

    def findMatchingParentheses(self, expression):
        stack = []
        parenthesisTuples = {}
        for index, char in enumerate(expression):
            if char == "(":
                stack.append(index)
            elif char == ")":
                parenthesisTuples[stack.pop()] = index
        return parenthesisTuples


if __name__ == '__main__':
    sol = Solution()
    print(sol.parseBoolExpr("|(&(t,f,t),!(t))"), "false")
    print(sol.parseBoolExpr("&(t,f)"), "false")
    print(sol.parseBoolExpr("|(f,t)"), "true")
    print(sol.parseBoolExpr("!(f)"), "true")
    print(sol.parseBoolExpr("!(&(!(t),&(f),|(f)))"), "true")
    print(sol.parseBoolExpr("!(&(!(&(f)),&(t),|(f,f,t)))"), "False")