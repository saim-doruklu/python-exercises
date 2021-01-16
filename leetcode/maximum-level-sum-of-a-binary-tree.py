# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_depth = 1
        this_level = [root]
        next_level = []
        max_level_sum = -999999999999999
        max_level = None
        while len(this_level):
            level_sum = 0
            for node in this_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
                level_sum += node.val
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level_depth
            this_level = next_level
            next_level = []
            level_depth += 1
        return max_level, max_level_sum

    def convert_to_tree(self, nodes: List, index, nodes_in_prev_level: List[TreeNode], is_root):
        nodes_in_level = []
        root = None
        if is_root:
            root = TreeNode(nodes[0])
            nodes_in_level.append(root)
        else:
            for index_in_level in range(2 * len(nodes_in_prev_level)):
                if index + index_in_level < len(nodes):
                    value = nodes[index + index_in_level]
                    if value is not None:
                        node = TreeNode(value)
                        parent = nodes_in_prev_level[index_in_level // 2]
                        if index_in_level % 2 == 0:
                            parent.left = node
                        else:
                            parent.right = node
                        nodes_in_level.append(node)
        if len(nodes_in_level):
            next_level_index = 1 if is_root else index + (2 * len(nodes_in_prev_level))
            self.convert_to_tree(nodes, next_level_index, nodes_in_level, False)
        return root


if __name__ == '__main__':
    solution = Solution()
    root = solution.convert_to_tree([989, None, 10250, 98693, -89388, None, None, None, -32127], 0, [], True)
    print(solution.maxLevelSum(root))
    root = solution.convert_to_tree([1, 7, 0, 7, -8, None, None], 0, [], True)
    print(solution.maxLevelSum(root))
    root = solution.convert_to_tree([1, 1, 0, 7, -8, -7, 9], 0, [], True)
    print(solution.maxLevelSum(root))
