

class Node(object):
    def __init__(self, value ) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:

        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node, value):
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)

            return node

        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node) -> None:
            # Inorder Left, Root, Right
            # Preorder Root, Left, Right
            # Postorder Left, Right, Root
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def search(self, value:int) -> bool:
        def _search(node, value: int):
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    #どれが最も小さいNodeかをみていく作業
    def min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value: int) -> None:
        def _remove(node, value):
            if node is None:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right,value)

            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        return _remove(self.root, value)




if __name__ == '__main__':
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(10)
    binary_tree.insert(2)

    binary_tree.inorder()
    root = None
    # inorder(root)
    # print(root.value)
    # print(root.right.value)
    # print(root.right.left.value)
    # print(root.right.right.value)
    # inorder(root)
    # print('############# Remove')
    # root = remove(root, 6)
    # inorder(root)
