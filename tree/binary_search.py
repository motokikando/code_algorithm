

class Node(object):
    def __init__(self, value ) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):

    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node

def inorder(node) -> None:
    # Inorder Left, Root, Right
    # Preorder Root, Left, Right
    # Postorder Left, Right, Root
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node, value: int):
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    elif node.value < value:
        return search(node.right, value)

if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    # inorder(root)
    print(root.value)
    print(root.right.value)
    print(root.right.left.value)
    print(root.right.right.value)
