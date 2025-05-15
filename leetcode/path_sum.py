from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


def solve(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, current_sum):
        if not root:
            return False

        current_sum += root.val
        
        if not root.left and not root.right:  # not a leaf node
            return current_sum == targetSum

        return dfs(root.left, current_sum) or dfs(root.right, current_sum)
    
    return dfs(root, 0)


if __name__ == "__main__":
    root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = to_binary_tree(root)
    targetSum = 22
    expected = True
    ans = solve(root=root, targetSum=targetSum)
    print(ans, expected)
