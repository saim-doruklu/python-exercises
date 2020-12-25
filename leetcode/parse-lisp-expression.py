import re


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

    def evaluate_in_env(self, expression, env_stack):

        if type(expression) == str:
            if self.is_number(expression):
                return int(expression)
            else:
                return int(self.find_in_env(env_stack, expression))

        symbols = {}
        env_stack.append(symbols)

        function_type = expression[0]
        if function_type == "add" or function_type == "mult":
            def calculate(x, y):
                if function_type == "add":
                    return x + (y or 0)
                else:
                    return x * (y or 1)

            cumulative_result = None
            for sub_expression in expression[1:]:
                evaluated_value = self.evaluate_in_env(sub_expression, env_stack)
                cumulative_result = calculate(evaluated_value, cumulative_result)

            expression_evaluation_result = cumulative_result
        else:
            last_expr_index = expression.__len__() - 1
            for index in range(1, last_expr_index + 1, 2):
                if index == last_expr_index:
                    expression_evaluation_result = self.evaluate_in_env(expression[index], env_stack)
                else:
                    new_symbol = expression[index]
                    value = self.evaluate_in_env(expression[index + 1], env_stack)
                    symbols[new_symbol] = value

        env_stack.pop()
        return expression_evaluation_result

    def find_in_env(self, env_stack: list, symbol):
        for index in range(0, env_stack.__len__()):
            current_env = env_stack[-index - 1]
            if current_env.get(symbol) is not None:
                return current_env.get(symbol)

    def is_number(self, string):
        return re.match(r"-?\d+", string)


if __name__ == '__main__':
    sol = Solution()
    print(sol.evaluate("(add 1 2)"), 3)
    print(sol.evaluate("(add (add 3 4) 2)"), 9)
    print(sol.evaluate("(mult 3 (add 2 3))"), 15)
    print(sol.evaluate("(let x 2 (mult x 5))"), 10)
    print(sol.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"), 14)
    print(sol.evaluate("(let x 3 x 2 x)"), 2)
    print(sol.evaluate("(let x 1 y 2 x (add x y) (add x y))"), 5)
    print(sol.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"), 6)
    print(sol.evaluate("(let a1 3 b2 (add a1 1) b2)"), 4)
    print(sol.evaluate("(let x 7 -12)"), -12)
    print(sol.evaluate("(let x -2 y x y)"), -2)
