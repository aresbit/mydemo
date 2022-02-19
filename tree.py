class tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

def size(t):
    if t is None:
        return 0
    else:
        return size(t.left) + 1 + size(t.right)


def height(t):
    if t is None:
        return 0
    else:
        return max(height(t.left), height(t.right)) + 1

def sum_tree(t):
    if t is None:
        return 0
    else:
        return sum_tree(t.left) + t.data + sum_tree(t.right)

if __name__ == '__main__':
    t = tree(1)
    t.left = tree(2)
    t.right = tree(3)
    t.left.left = tree(4)
    t.left.right = tree(5)
    print(size(t))
    print(size(None))
    print(height(t))
    print(height(None))
    print(sum_tree(t))
    print(sum_tree(None))
    print(sum_tree(tree(1)))

