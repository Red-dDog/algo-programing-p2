class Node:
    """Вузол червоно-чорного дерева."""
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = 1  # 1 - Червоний, 0 - Чорний
        self.parent = None
        self.left = None
        self.right = None

class RedBlackPriorityQueue:
    """Черга з пріоритетами на основі червоно-чорного дерева."""
    
    def __init__(self):
        self.TNULL = Node(None, None)
        self.TNULL.color = 0
        self.TNULL.left = self.TNULL
        self.TNULL.right = self.TNULL
        self.root = self.TNULL

    def insert(self, value, priority):
        """Вставляє елемент із заданим значенням та пріоритетом."""
        node = Node(value, priority)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.priority >= x.priority:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.priority >= y.priority:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self._insert_fixup(node)

    def extract_max(self):
        """Видаляє та повертає елемент (value, priority) з найвищим пріоритетом."""
        if self.root == self.TNULL:
            return None

        z = self.root
        while z.left != self.TNULL:
            z = z.left

        result = (z.value, z.priority)

        y = z
        y_original_color = y.color
        x = z.right

        if z.parent is None:
            self.root = x
        elif z == z.parent.left:
            z.parent.left = x
        else:
            z.parent.right = x
        x.parent = z.parent

        if y_original_color == 0:
            self._delete_fixup(x)

        return result

    def peek(self):
        """Повертає елемент (value, priority) з найвищим пріоритетом без видалення."""
        if self.root == self.TNULL:
            return None

        z = self.root
        while z.left != self.TNULL:
            z = z.left

        return (z.value, z.priority)
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
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

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
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

    def _insert_fixup(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Дядько (Uncle)
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Дядько (Uncle)
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def _delete_fixup(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right  # Брат (Sibling)
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self._right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left  # Брат (Sibling)
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self._left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0
        