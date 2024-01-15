class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._node_count = 0

    def insert(self, value):
        if self._root is None:
            self._root = self.Node(value)
        else:
            self._insert(self._root, value)
        self._node_count += 1

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert(node.right, value)

    def get_node_count(self):
        return self._node_count
    
    def print_values(self):
        self._in_order_traversal(self._root)

    def _in_order_traversal(self, node):
        if node is None:
            return
        self._in_order_traversal(node.left)
        print(node.value, end=' ')
        self._in_order_traversal(node.right)

    def delete_tree(self):
        self._root = None
        self._node_count = 0

    def is_in_tree(self, value):
        return self._is_in_tree(self._root, value)
    
    def _is_in_tree(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._is_in_tree(node.left, value)
        else:
            return self._is_in_tree(node.right, value)
        
    def get_height(self):
        return self._get_height(self._root)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return max(self._get_height(node.left), self._get_height(node.right)) + 1
    
    def get_min(self):
        node = self._root 
        if node:
            while node.left is not None:
                node = node.left 
        return node.value
    
    def get_max(self):
        node = self._root 
        if node:
            while node.right is not None:
                node = node.right 
        return node.value
    
    def is_binary_search_tree(self):
        return self._is_binary_search_tree(self._root, float('-inf'), float('inf'))
    
    def _is_binary_search_tree(self, node, min_value, max_value):
        if node is None:
            return True 
        if node.value < min_value or node.value > max_value:
            return False 
        return self._is_binary_search_tree(node.left, min_value, node.value) and self._is_binary_search_tree(node.right, node.value, max_value)

    def delete_value(self, value):
        self._root = self._delete_value(self._root, value)

    def _delete_value(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_value(node.left, value)
        elif value > node.value:
            node.right = self._delete_value(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.value = self._find_min_value(node.right)
                node.right = self._delete_value(node.right, node.value)
        return node
    
    def _find_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value
    
    def get_successor(self, value):
        node = self._root
        successor = None
        while node is not None:
            if value < node.value:
                successor = node
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                if node.right is not None:
                    successor = self._find_min_node(node.right)
                break
        return successor
    
    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    




tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.print_values()
print()
print(f'Number of nodes: {tree.get_node_count()}')
print(tree.is_in_tree(3))
print(tree.is_in_tree(9))
print(tree.get_min())
print(tree.get_max())
print(tree.get_height())
print(tree.is_binary_search_tree())
tree.delete_value(5)
tree.print_values()


