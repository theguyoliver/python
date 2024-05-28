class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # Remember the init block is just like a constructor that holds parameters we want to enter into
    # the class. So our data is that parameter, it can be a string, int, etc
    # Also, every item/child in children is an instance of TreeNode because it is also a tree if its own

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode('Mobile Phones')

    iPhone = TreeNode('iPhone')
    iPhone.add_child(TreeNode('iPhone12'))
    iPhone.add_child(TreeNode('iPhone14 Pro'))
    iPhone.add_child(TreeNode('iPhone15'))

    samsung = TreeNode('Samsung')
    samsung.add_child(TreeNode('Samsung A12'))
    samsung.add_child(TreeNode('Samsung A31'))
    samsung.add_child(TreeNode('Samsung S24 Ultra'))

    pixel = TreeNode('Google Pixel')
    pixel.add_child(TreeNode('Pixel 7'))
    pixel.add_child(TreeNode('Pixel 7A'))
    pixel.add_child(TreeNode('Pixel 8'))

    root.add_child(iPhone)
    root.add_child(samsung)
    root.add_child(pixel)

    return root


if __name__ == '__main__':
    tree = build_product_tree()
    tree.print_tree()
