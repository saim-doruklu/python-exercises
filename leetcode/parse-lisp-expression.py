from __future__ import annotations
import re
# from typing import List, Tuple, Union

class Expression:

    def __init__(self, parent):
        self.parent = parent
        self.expressions = []
        self.env = {}

    def add_expression(self, expression):
        self.expressions.append(expression)

    def find_in_env(self, symbol):
        current_env = self
        while current_env.env.get(symbol) is None:
            current_env = current_env.parent
        return current_env.env.get(symbol)


class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = re.findall(r"(\(|[-\w]+|\))", expression)
        current_expression = Expression(None)
        for token in tokens:
            if token == "(":
                sub_expression = Expression(current_expression)
                current_expression.add_expression(sub_expression)
                current_expression = sub_expression
            elif token == ")":
                current_expression = current_expression.parent
            else:
                current_expression.add_expression(token)
        return self.evaluate_in_env(current_expression.expressions[0])

    def evaluate_in_env(self, expression):
        expression_type = expression.expressions[0]

        if expression_type == "add" or expression_type == "mult":
            def function_add(x):
                return x + cumulative_result

            def function_mult(x):
                return x * cumulative_result

            if expression_type == "add":
                cumulative_result = 0
                current_function = function_add
            else:
                cumulative_result = 1
                current_function = function_mult

            for sub_expression in expression.expressions[1:]:
                evaluated_value = self.evaluate_value_or_expression(expression, sub_expression)
                cumulative_result = current_function(evaluated_value)

            return cumulative_result
        else:
            last_expr_index = expression.expressions.__len__()
            for index in range(1, last_expr_index, 2):
                if index == last_expr_index - 1:
                    return self.evaluate_value_or_expression(expression, expression.expressions[index])
                else:
                    symbol = expression.expressions[index]
                    value = self.evaluate_value_or_expression(expression, expression.expressions[index+1])
                    expression.env[symbol] = value

    def evaluate_value_or_expression(self, expression, sub_expression):
        if type(sub_expression) == str:
            if self.is_number(sub_expression):
                evaluated_value = int(sub_expression)
            else:
                evaluated_value = int(expression.find_in_env(sub_expression))
        else:
            evaluated_value = self.evaluate_in_env(sub_expression)
        return evaluated_value

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
