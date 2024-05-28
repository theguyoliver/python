class TreeNode:
    def __init__(self, location_name):
        self.name = location_name
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

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_location_tree():
    ww = TreeNode('Global')

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bangluru'))
    karnataka.add_child(TreeNode('Mysore'))

    india = TreeNode('India')
    india.add_child(gujarat)
    india.add_child(karnataka)

    nj = TreeNode('New Jersey')
    nj.add_child(TreeNode('Princeton'))
    nj.add_child(TreeNode('Trenton'))

    cali = TreeNode('California')
    cali.add_child(TreeNode('San Francisco'))
    cali.add_child(TreeNode('Mountain View'))
    cali.add_child(TreeNode('Palo Alto'))

    us = TreeNode('USA')
    us.add_child(nj)
    us.add_child(cali)

    ww.add_child(india)
    ww.add_child(us)

    return ww


if __name__ == '__main__':
    tree = build_location_tree()
    tree.print_tree(0)
    tree.print_tree(1)
