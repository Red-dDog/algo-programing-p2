class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def find_successor(self, node: 'BinaryTree') -> 'BinaryTree':
        if node is None:
            return None
        
        if node.right is not None:
            current = node.right
            while current.left is not None:
                current = current.left
            return current
            
        current_node = node
        parent_node = node.parent
        while parent_node is not None and current_node == parent_node.right:
            current_node = parent_node
            parent_node = parent_node.parent
        
        return parent_node

#       10
#      /  \
#     5    15
#    / \     \
#   3   7     20
#            /
#           12

node10 = BinaryTree(10)
node5 = BinaryTree(5)
node15 = BinaryTree(15)
node3 = BinaryTree(3)
node7 = BinaryTree(7)
node20 = BinaryTree(20)
node12 = BinaryTree(12)

node10.left = node5
node10.right = node15

node5.left = node3
node5.right = node7
node5.parent = node10

node15.right = node20
node15.parent = node10

node3.parent = node5

node7.parent = node5

node20.left = node12
node20.parent = node15
node12.parent = node20

def print_test_result(node_name, node_object):
    successor = BinaryTree.find_successor(node10, node_object)
    successor_val = successor.value if successor else "None"
    print(f"Successor of {node_name} ({node_object.value}): {successor_val}")

print("--- Testing find_successor with the example tree ---")
print("In-order traversal order is: 3, 5, 7, 10, 12, 15, 20\n")

print_test_result("node7", node7)   # Expect 10
print_test_result("node10 (root)", node10)  # Expect 12
print_test_result("node15", node15)  # Expect 20
print_test_result("node5", node5)    # Expect 7
print_test_result("node20", node20)  # Expect None

print_test_result("node3", node3)
print_test_result("node12", node12)