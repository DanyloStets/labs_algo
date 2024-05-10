from collections import deque
BLACK = True
RED = False
class Node:
    def __init__(self, key, value):
        self.key = key
        self.parent = None 
        self.color = RED
        self.left = None
        self.right = None
        self.value = value

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(1, 100)
        self.NIL.color = BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def insert(self, key, value):
        z = Node(key, value)
        z.left = self.NIL
        z.right = self.NIL
        y = None 
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left 
            else:
                x = x.right 
        z.parent = y 
        if y == None:
            self.root = z 
        elif z.key < y.key: 
            y.left = z 
        else:
            y.right = z

        self.insert_fixup(z)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left 

        if y.left != self.NIL:
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

        if y.right != self.NIL:
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

    def insert_fixup(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right 
                if y.color == RED:
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
            else:
                y = z.parent.parent.left 
                if y.color == RED:
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
            if z == self.root:
                break
        self.root.color = BLACK

    def delete(self, k=None):
        if k == None:
            z = self.root

        z = self.search(k)

        if z == self.NIL:
            return "Key not found!"

        y = z
        y_orig_color = y.color 
        
        # case 1
        if z.left == self.NIL:
            x = z.right 
            self.transplant(z, z.right)
        # case 2
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        # case 3
        else:
            y = self.minimum(z.right)
            y_orig_color = y.color
            x = y.right 
            
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self.transplant(z, y)
            y.left = z.left 
            y.left.parent = y 
            y.color = z.color 
        
        if y_orig_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                # type 1
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                # type 2
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED 
                    x = x.parent 
                else:
                    # type 3
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    # type 4
                    w.color = x.parent.color 
                    x.parent.color = BLACK 
                    w.right.color = BLACK 
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                # type 1
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                # type 2
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED 
                    x = x.parent 
                else:
                    # type 3
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left
                    # type 4
                    w.color = x.parent.color 
                    x.parent.color = BLACK 
                    w.left.color = BLACK 
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v 
        else:
            u.parent.right = v
        v.parent = u.parent 

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def search(self, k):
        x = self.root
        while x != self.NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def print_tree(self, print_color=False):
        queue = deque()
        queue.append(self.root)

        while(queue):
            node = queue.popleft()

            if print_color:
                print(f'{node.key}{node.print_color()}', end=' ')
            else:
                print(node.key, end=' ')

            if node.left != self.NIL:
                queue.append(node.left)
            if node.right != self.NIL:
                queue.append(node.right)

