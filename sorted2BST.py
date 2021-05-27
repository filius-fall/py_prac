class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def sorted2BST(nums,left,right):
    if left == right:
        return None

    mid = (left + right) >> 1
    node = TreeNode(nums[mid])
    node.left = sorted2BST(nums,left,mid)
    node.right = sorted2BST(nums,mid+1,right)
    return node