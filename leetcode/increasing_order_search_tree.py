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


def solve(root: Optional[TreeNode]) -> Optional[TreeNode]:
    pass


if __name__ == "__main__":
    root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    root = to_binary_tree(root)
    print(root.right.val)
    # expected = [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9]
    # ans = solve(root=root)
    # print(expected, ans)
