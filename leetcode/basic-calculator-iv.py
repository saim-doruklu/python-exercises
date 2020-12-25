import re
from typing import List


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        var_to_value = {}
        for index, var in enumerate(evalvars):
            var_to_value[var] = evalints[index]
        tokens = re.findall("[(+\-*)]|[a-z]+|\d+", expression)
        expression_tree = self.generate_tree(tokens, var_to_value)
        result = self.solve(expression_tree)
        result_by_degree = {}
        for key in sorted(result):
            list = result[key][0]
            value = result[key][1]
            if result_by_degree.get(list.__len__()) is None:
                result_by_degree[list.__len__()] = []
            expression = str(value)
            if list.__len__() > 0:
                expression += "*" + "*".join(list)
            result_by_degree[list.__len__()].append(expression)
        final_result = []
        for key in reversed(sorted(result_by_degree)):
            for value in result_by_degree[key]:
                final_result.append(value)
        return final_result

    def generate_tree(self, tokens, eval_vars):
        expression_depth = []
        current_expression = []
        for token in tokens:
            if token != "(" and token != ")":
                if str.isalpha(token) and eval_vars.get(token) is not None:
                    current_expression.append(eval_vars.get(token))
                else:
                    current_expression.append(token)
            elif token == "(":
                sub_expression = []
                current_expression.append(sub_expression)
                expression_depth.append(current_expression)
                current_expression = sub_expression
            else:
                current_expression = expression_depth.pop()
        return current_expression

    def solve(self, expression_list) -> dict:
        sum_so_far = {}
        previous_multiplier = None
        index = 0
        last_operation = "+"
        while index < expression_list.__len__():
            raw_expression = expression_list[index]
            if type(raw_expression) == int or (type(raw_expression) == str and str.isnumeric(raw_expression)):
                if int(raw_expression) != 0:
                    evaluated_expression = {"[]": [[], int(raw_expression)]}
                else:
                    evaluated_expression = {}
            elif type(raw_expression) == str:
                evaluated_expression = {str([raw_expression]): [[raw_expression], 1]}
            else:
                evaluated_expression = self.solve(raw_expression)

            if previous_multiplier is not None:
                evaluated_expression = self.multiply(evaluated_expression, previous_multiplier)

            if index < expression_list.__len__() - 1 and expression_list[index + 1] == "*":
                previous_multiplier = evaluated_expression
            else:
                sum_so_far = self.sum(sum_so_far, evaluated_expression, last_operation)

            if index < expression_list.__len__() - 1 and expression_list[index + 1] != "*":
                last_operation = expression_list[index + 1]
                previous_multiplier = None

            index = index + 2
        return sum_so_far

    def sum(self, expr_one: dict, expr_two: dict, last_operation):
        for key in expr_two.keys():
            expr_one_multiplier = expr_one.get(key)[1] if expr_one.get(key) else 0
            key_as_list = expr_two.get(key)
            expr_two_multiplier = key_as_list[1]
            if last_operation == "+":
                result = expr_one_multiplier + expr_two_multiplier
            else:
                result = expr_one_multiplier - expr_two_multiplier

            if result == 0:
                expr_one.pop(key)
            else:
                expr_one[key] = [key_as_list[0], result]
        return expr_one

    def multiply(self, expr_one: dict, expr_two: dict):
        result = {}
        for key_one in expr_one.keys():
            for key_two in expr_two.keys():
                multiplication = self.multiply_single(expr_one[key_one][0], expr_one[key_one][1], expr_two[key_two][0],
                                                      expr_two[key_two][1])
                self.sum(result, multiplication, "+")

        return result

    def multiply_single(self, key_one_list: list, value_one, key_two_list: list, value_two):
        new_key = key_one_list + key_two_list
        new_key.sort()
        return {str(new_key): [new_key, value_one * value_two]}


if __name__ == '__main__':
    solution = Solution()
    print(solution.basicCalculatorIV(expression="e + 8 - a + 5", evalvars=["e"], evalints=[1]) == ["-1*a", "14"])
    print(solution.basicCalculatorIV(expression="e + 8 - a + a + 5", evalvars=["e"], evalints=[1]) == ["14"])
    print(solution.basicCalculatorIV(expression="((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                                     evalvars=[], evalints=[]) == ["-1*a*a*b*b", "2*a*a*b*c", "-1*a*a*c*c", "1*a*b*b*b",
                                                                   "-1*a*b*b*c", "-1*a*b*c*c", "1*a*c*c*c",
                                                                   "-1*b*b*b*c", "2*b*b*c*c", "-1*b*c*c*c", "2*a*a*b",
                                                                   "-2*a*a*c", "-2*a*b*b", "2*a*c*c", "1*b*b*b",
                                                                   "-1*b*b*c", "1*b*c*c", "-1*c*c*c", "-1*a*a", "1*a*b",
                                                                   "1*a*c", "-1*b*c"])
    print(solution.basicCalculatorIV(expression="e - 8 + temperature - pressure", evalvars=["e", "temperature"],
                                     evalints=[1, 12]) == ["-1*pressure", "5"])
    print(solution.basicCalculatorIV(expression="(e + 8) * (e - 8)", evalvars=[], evalints=[]) == ["1*e*e", "-64"])
    print(solution.basicCalculatorIV(expression="0", evalvars=[], evalints=[]) == [])
