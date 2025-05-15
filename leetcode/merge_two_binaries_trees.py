# Definition for a binary tree node.
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


def solve(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
        return None
    
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    root = TreeNode(v1 + v2)
    root.left = solve(root1.left if root1 else None, root2.left if root2 else None)
    root.right = solve(root1.right if root1 else None, root2.right if root2 else None)

    return root


if __name__ == "__main__":
    root1 = to_binary_tree([1,3,2,5])
    root2 = to_binary_tree([2,1,3,None,4,None,7])
    expected = [3,4,5,5,4,None,7]
    ans = solve(root1=root1, root2=root2)
    print(expected, ans)
