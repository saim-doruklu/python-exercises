from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return [int(x) for x in (list(str(sum([x * (10 ** (A.__len__()-1-index)) for index, x in enumerate(A)])+K)))]

if __name__ == '__main__':
    solution = Solution()
    print(solution.addToArrayForm([1,2,0,0],34))