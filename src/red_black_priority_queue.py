RED = True
BLACK = False
class Node():
    def __init__(self, value, priority, color=RED):
        self.priority = priority
        self.color = color
        self.right = None
        self.left = None
        self.value = value
        self.parent = None

class RedBlackTree():
    def __init__(self, ):
        self.root = None

    def insert(self, value, priority):
        z = Node(value, priority)
        y = None
        x = self.root
        if x is None:
            self.root = Node(value, priority, color=BLACK)
            return
        while x is not None:
            y = x
            if priority > x.priority:
                x = x.right
            else:
                x = x.left  
        z.parent = y
        if priority > y.priority:
            y.right = z
        else:
            y.left = z
        self.insert_fix(z)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left 
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent 
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y 
        y.left = x 
        x.parent = y

    def right_rotate(self, x):
        y = x.left 
        x.left = y.right 
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent 
        if x.parent is None:
            self.root = y 
        elif x == x.parent.right:
            x.parent.right = y 
        else:
            x.parent.left = y 
        y.right = x 
        x.parent = y

    def insert_fix(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                self.key_in_left(z)
            else:
                self.key_in_right(z)
            if z == self.root:
                break
        self.root.color = BLACK        

    def key_in_left(self, z):
        y = z.parent.parent.right
        if y and y.color == RED:
            z.parent.color = BLACK
            y.color = BLACK
            z.parent.parent.color = RED
            z = z.parent.parent
        else:
            if z == z.parent.right:
                z = z.parent
                self.left_rotate(z)
            z.parent.color = BLACK
            z.parent.parent.color = RED
            self.right_rotate(z.parent.parent)

    def key_in_right(self, z):
        y = z.parent.parent.left
        if y and y.color == RED:
            z.parent.color = BLACK
            y.color = BLACK
            z.parent.parent.color = RED
            z = z.parent.parent
        else:
            if z == z.parent.left:
                z = z.parent
                self.right_rotate(z)
            z.parent.color = BLACK
            z.parent.parent.color = RED
            self.left_rotate(z.parent.parent)
    
    def search_most_priority(self):
        x = self.root
        while x.right:
            x = x.right
        return x

    def delete(self):
        z = self.search_most_priority()
        node_to_deleted = z
        z_color = z.color

        if z.left is None:
            z.color = z.parent.color
            z = z.parent
        else:
            z.color = z.left.color
            z.left.parent = z.parent
            z = z.left
        if z_color == BLACK:
            self.delete_fixup(z)
        return node_to_deleted.priority


    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED 
                    x = x.parent 
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color 
                    x.parent.color = BLACK 
                    w.right.color = BLACK 
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED 
                    x = x.parent 
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color 
                    x.parent.color = BLACK 
                    w.left.color = BLACK 
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

def inorder_tree(self, node):
        if node is None:
            return

        self.inorder_tree(node.left)
        print(node.color)
        print(node.priority)
        self.inorder_tree(node.right)

# tree = RedBlackTree()
# tree.insert(1, 11)
# tree.insert(30, 10)
# tree.insert(11, 6)
# tree.insert(12, 7)
# tree.insert(13, 3)
# tree.insert(14, 1)
# tree.insert(15, 8)
# tree.insert(16, 4)
# print(tree.delete())
# print(tree.root.color)
# print(tree.root.priority)