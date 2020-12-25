import re


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


initial_args = {
    "add": 0,
    "mult": 1,
}


class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = re.findall(r"(\(|[-\w]+|\))", expression)
        expression_depth = []
        current_expression = []
        for token in tokens:
            if token == "(":
                sub_expression = []
                current_expression.append(sub_expression)
                expression_depth.append(current_expression)
                current_expression = sub_expression
            elif token == ")":
                current_expression = expression_depth.pop()
            else:
                current_expression.append(token)
        return self.evaluate_in_env(current_expression[0], [])

    def evaluate_in_env(self, expression, env_stack, index=0, function_type=None, symbol=None):

        if function_type is None:
            function_type = expression[0]
            symbols = {}
            env_stack.append(symbols)
            return self.evaluate_in_env(expression, env_stack, 1, function_type, initial_args.get(function_type))

        sub_expression = expression[index]
        is_last_sub_expression = index == expression.__len__() - 1
        if function_type == "let" and symbol is None and not is_last_sub_expression:
            return self.evaluate_in_env(expression, env_stack, index + 1, function_type, sub_expression)

        if type(sub_expression) == str:
            if self.is_number(sub_expression):
                current_result = int(sub_expression)
            else:
                current_result = self.find_in_env(env_stack, sub_expression)
        else:
            current_result = self.evaluate_in_env(sub_expression, env_stack)

        if is_last_sub_expression:
            env_stack.pop()
            return current_result

        if function_type == "let":
            env_stack[-1][symbol] = current_result

        evaluate_remaining = self.evaluate_in_env(expression, env_stack, index + 1, function_type)

        if function_type == "add":
            return current_result + evaluate_remaining
        elif function_type == "mult":
            return current_result * evaluate_remaining
        else:
            return evaluate_remaining

    def find_in_env(self, env_stack: list, symbol):
        for index in range(0, env_stack.__len__()):
            current_env = env_stack[-index - 1]
            if current_env.get(symbol) is not None:
                return current_env.get(symbol)

    def is_number(self, string):
        return re.match(r"-?\d+", string)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.evaluate("(add 1 2)"), 3)
    # print(sol.evaluate("(add (add 3 4) 2)"), 9)
    # print(sol.evaluate("(mult 3 (add 2 3))"), 15)
    print(sol.evaluate("(let x 2 (mult x 5))"), 10)
    print(sol.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"), 14)
    print(sol.evaluate("(let x 3 x 2 x)"), 2)
    print(sol.evaluate("(let x 1 y 2 x (add x y) (add x y))"), 5)
    print(sol.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"), 6)
    print(sol.evaluate("(let a1 3 b2 (add a1 1) b2)"), 4)
    print(sol.evaluate("(let x 7 -12)"), -12)
    print(sol.evaluate("(let x -2 y x y)"), -2)
    print(sol.evaluate(
        "(let var0 -2 var1 -1 var2 -1 var3 -3 var4 4 var5 -3 var6 3 var7 4 var8 -3 var9 0 var10 1 var11 2 var12 -3 var13 3 var14 -5 var15 -5 var16 3 var17 -3 var18 0 var19 3 var20 -5 var21 -2 var22 -3 var23 -2 var24 -2 var25 -3 var26 -4 var27 4 var28 -4 var29 1 (mult (let var0 2 var3 4 var6 1 var9 1 var12 1 var15 -1 var18 -1 var21 -1 var24 0 var27 2 (add (mult var12 (add (mult var4 var7) (mult var24 -1))) (mult -21 (let var0 -4 var6 0 var12 -2 var18 4 var24 1 (mult (add (mult var18 var22) (add (add (mult 1 1) -6) -3)) (add (mult (mult -22 (mult 1 1)) (add -21 var26)) (mult -22 (add (mult 1 1) var28)))))))) (add var28 (add (add (add var3 -22) (mult (mult -7 (mult (mult -8 (let var0 0 var10 3 var20 3 (mult 1 1))) -6)) var15)) (mult (mult (mult var4 (add (add (add (mult 1 1) -7) (add var7 var22)) var2)) (let var0 1 var7 -5 var14 -5 var21 -3 var28 -2 (let var0 0 var8 -5 var16 0 var24 2 (add -30 var15)))) var18)))))"),
        427173136)
