class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

arr = []
def print_tree(k):
    if k is None:
        return
    # if k.left is None:
    #     arr.append(None)
    # else:
    print_tree(k.left)
    arr.append(k.data)
    print_tree(k.right)


# node = TreeNode(1)
# node.left = TreeNode(3)
# node.right = TreeNode(3)
# node.left.left = TreeNode(4)

# print_tree(node)


# def isSameTree(p,q):
#     arr = []
#     def print_tree(k):
#         if k is None:
#             return
#         print_tree(k.left)
#         arr.append(k.data)
#         print(arr)
#         print_tree(k.right)

#     if print_tree(p) == print_tree(q):
#         print(p,q)
#     else:
#         return False



node1 = TreeNode(1)
node1.left = TreeNode(2)
print_tree(node1)
print(arr)
arr = []

node2 = TreeNode(1)
node2.right = TreeNode(2)
print_tree(node2)
print(arr)
