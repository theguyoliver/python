class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search_tree(self, value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left:
                self.left.search_tree(value)
            else:
                return False
        else:
            if self.right:
                self.right.search_tree(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        if self.left:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        if self.right:
            return self.right.find_max()

    def calculate_sum(self):
        if self.data is None:
            return 0
        if self.left:
            x = self.left.calculate_sum()
        else:
            x = 0
        if self.right:
            y = self.right.calculate_sum()
        else:
            y = 0

        return x + y + self.data

        # elements = []
        #
        # if self.left:
        #     elements += self.left.calculate_sum()
        #
        # elements.append(self.data)
        #
        # if self.right:
        #     elements += self.right.calculate_sum()
        #
        # return sum(elements)

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return sum(elements)

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        #    max_val = self.left.find_max()
        #    self.data = max_val
        #    self.left = self.left.delete(max_val)
        return self


def build_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child(elements[i])

    return root_node


if __name__ == '__main__':
    numbers = [17, 3, 8, 13, 27, 53, 12, 19]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    numbers_tree.delete(8)
    print(numbers_tree.in_order_traversal())
