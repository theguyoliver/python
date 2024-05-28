class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, action):
        if action == 'name':
            output = self.name
        elif action == 'designation':
            output = self.designation
        else:
            output = self.name + ' (' + self.designation + ')'

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + output)
        if self.children:
            for child in self.children:
                child.print_tree(action)


def build_management_tree():
    ceo = TreeNode('Nilupul', 'CEO')

    cto = TreeNode('Chinmay', 'CTO')
    ih = TreeNode('Vishwa', 'Infrastructure Head')
    ih.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    ih.add_child(TreeNode('Abhijit', 'App manager'))
    cto.add_child(ih)
    cto.add_child(TreeNode('Aamir', 'Application Head'))

    hrh = TreeNode('Gels', 'HR Head')
    hrh.add_child(TreeNode('Peter', 'Recruitment Manager'))
    hrh.add_child(TreeNode('Waqas', 'Policy Manager'))

    ceo.add_child(cto)
    ceo.add_child(hrh)

    return ceo


def build_location_tree():
    ww = TreeNode('Global')


if __name__ == '__main__':
    tree = build_management_tree()
    tree.print_tree('name')
    tree.print_tree('both')
