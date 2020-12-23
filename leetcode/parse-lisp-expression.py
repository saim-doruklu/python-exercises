# from __future__ import annotations
from typing import List, Tuple


class ListNode(object):
    def __init__(self, x: str):
        self.val = x
        self.next = None

    def get_next(self):
        return self.next

    def get_next_n(self, n_times):
        result = self
        for i in range(n_times):
            result = result.next
        return result

    def set_next(self, next_node):
        self.next = next_node

    def get_val(self) -> str:
        return self.val


class Solution:
    def evaluate(self, expression: str) -> int:
        expression_pointer, result = self.evaluate_in_env([], self.string_to_list_node(expression))
        return result

    def evaluate_in_env(self, env_stack: List[dict], pointer: ListNode) -> Tuple[ListNode, int]:
        if self.is_number(pointer.val):
            pointer, word = self.get_next_word(pointer)
            return pointer, self.evaluate_int_or_symbol(env_stack, word)

        pointer = pointer.get_next()
        if self.is_number(pointer.val):
            pointer, word = self.get_next_word(pointer)
            return pointer.get_next(), self.evaluate_int_or_symbol(env_stack, word)

        result = None
        this_env = dict()
        env_stack.append(this_env)
        pointer, operation = self.get_next_word(pointer)
        if operation == "add" or operation == "mult":
            if operation == "add":
                cumulative_result = 0
            else:
                cumulative_result = 1

            while pointer.val != ")":
                pointer = pointer.get_next()
                if self.is_number_or_word(pointer.get_val()):
                    pointer, word = self.get_next_word(pointer)
                    next_value = self.evaluate_int_or_symbol(env_stack, word)
                else:
                    pointer, next_value = self.evaluate_in_env(env_stack, pointer)

                if operation == "add":
                    cumulative_result = cumulative_result + next_value
                else:
                    cumulative_result = cumulative_result * next_value

            result = cumulative_result
        else:
            is_final_expression = False
            while not is_final_expression:
                pointer = pointer.get_next()
                if self.is_word(pointer.val):
                    pointer, word = self.get_next_word(pointer)
                    if pointer.val != ")":
                        pointer = pointer.get_next()
                        if self.is_number_or_word(pointer.val):
                            pointer, to_eval = self.get_next_word(pointer)
                            this_env[word] = self.evaluate_int_or_symbol(env_stack, to_eval)
                        else:
                            pointer, this_env[word] = self.evaluate_in_env(env_stack,pointer)
                    else: # might be symbol or number, means this is final part of let
                        result = self.find_in_env(env_stack,word)
                        is_final_expression = True
                else: # either number or () expression, means this is final part of let
                    pointer, result = self.evaluate_in_env(env_stack, pointer)
                    is_final_expression = True
        env_stack.pop()
        pointer = pointer.get_next()
        return pointer, result

    def is_number(self, character):
        return str.isdigit(character) or character == "-"

    def is_word(self, character):
        return str.isalpha(character)

    def is_number_or_word(self, character):
        return self.is_number(character) or self.is_word(character)

    def evaluate_int_or_symbol(self, env_stack, word:str) -> int:
        if self.is_number(word[0]):
            return int(word)
        else:
            return self.find_in_env(env_stack, word)

    def find_in_env(self, env_stack:List[dict], word:str) -> int:
        for env in reversed(env_stack):
            if env.get(word) is not None:
                return env.get(word)

    def get_next_word(self, pointer) -> Tuple[ListNode, str]:
        word = []
        while self.is_number_or_word(pointer.val):
            word.append(pointer.val)
            pointer = pointer.get_next()
        word = "".join(word)
        return pointer, word

    def string_to_list_node(self, expression: str):
        previous_node = None
        first = None
        for i in expression:
            current_node = ListNode(i)
            if first is None:
                first = current_node
            if previous_node is not None:
                previous_node.set_next(current_node)
            previous_node = current_node
        return first


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
