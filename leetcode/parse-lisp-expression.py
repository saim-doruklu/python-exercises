from __future__ import annotations
import re


# from typing import List, Tuple, Union

class Expression:

    def __init__(self, parent_env):
        self.expressions = []
        self.env = {"0_parent_env":parent_env}

    def add_expression(self, expression):
        self.expressions.append(expression)



class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = re.findall(r"(\(|[-\w]+|\))", expression)
        expression_depth = []
        current_expression = Expression(None)
        for token in tokens:
            if token == "(":
                sub_expression = Expression(current_expression.env)
                current_expression.add_expression(sub_expression)
                expression_depth.append(current_expression)
                current_expression = sub_expression
            elif token == ")":
                current_expression = expression_depth.pop()
            else:
                current_expression.add_expression(token)
        return self.evaluate_in_env(current_expression.expressions[0])

    def evaluate_in_env(self, expression, parent_env=None):
        if type(expression) == str:
            if self.is_number(expression):
                return int(expression)
            else:
                return int(self.find_in_env(expression, parent_env))

        expression_type = expression.expressions[0]
        if expression_type == "add" or expression_type == "mult":
            def calculate(fun_type, x, y):
                if fun_type == "add":
                    return x + (y or 0)
                else:
                    return x * (y or 1)

            cumulative_result = None
            for sub_expression in expression.expressions[1:]:
                evaluated_value = self.evaluate_in_env(sub_expression, expression.env)
                cumulative_result = calculate(expression_type, evaluated_value, cumulative_result)

            return cumulative_result
        else:
            last_expr_index = expression.expressions.__len__() - 1
            for index in range(1, last_expr_index+1, 2):
                if index == last_expr_index:
                    return self.evaluate_in_env(expression.expressions[index], expression.env)
                else:
                    symbol = expression.expressions[index]
                    value = self.evaluate_in_env(expression.expressions[index + 1], expression.env)
                    expression.env[symbol] = value

    def is_number(self, string):
        return re.match(r"-?\d+", string)

    def find_in_env(self, symbol, current_env):
        while current_env.get(symbol) is None:
            current_env = current_env["0_parent_env"]
        return current_env.get(symbol)


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
