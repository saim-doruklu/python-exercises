from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carryOver = 1
        for digit in reversed(digits):
            digit = digit+carryOver
            if digit > 9:
                digit = 0
                carryOver = 1
            else:
                carryOver = 0
            result.append(digit)
        if carryOver > 0:
            result.append(1)
        return list(reversed(result))

if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9,9,9]))