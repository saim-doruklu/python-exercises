from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNumsWithIndexes = dict()
        for index, num in enumerate(nums):
            indexOfPair = previousNumsWithIndexes.get(target - num)
            if(indexOfPair != None):
                return [indexOfPair, index]
            else:
                previousNumsWithIndexes[num] = index


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([2,7,11,15], 9))
