class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def balanceBST(node):
    if node is None:
        return 0
    if node.left and node.right:
        return 1
    else:
        return 1 + max(balanceBST(node.left),balanceBST(node.right))


def balance(x):
    if abs(balanceBST(x.left)-balanceBST(x.right)) <= 1:
        return 1
    else:
        return 0



root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

k = balance(root)
print(k)