class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def is_sym(node):

    if node.left == node.right:
        return True


    return is_sym(node.left) and is_sym(node.righth)