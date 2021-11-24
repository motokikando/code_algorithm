

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

#どれが最も小さいNodeかをみていく作業
def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(node, value):
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right,value)

    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node




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
    # print(root.value)
    # print(root.right.value)
    # print(root.right.left.value)
    # print(root.right.right.value)
    inorder(root)
    print('############# Remove')
    root = remove(root, 6)
    inorder(root)
