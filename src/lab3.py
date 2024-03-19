class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_bigger(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    next_node = find_next_node(node)
    while next_node.value <= node.value:
        next_node = find_next_node(next_node)
    print(next_node.value)
    return next_node.value


def find_next_node(node):
    if node.right:
        return last_left_node(node.right)
    else:
        return find_upper_parent(node)


def find_upper_parent(node):
    current_node = node
    while current_node.parent and current_node.parent.right == current_node:
        current_node = current_node.parent
    return current_node.parent


def last_left_node(node):
    curent_node = node
    while curent_node.left:
        curent_node = curent_node.left
    return curent_node


# print(find_bigger(root, root.right.right.left))
