import time
nach = time.time()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _add_node(self, node, key):
        if key < node.key:
            if node.left:
                self._add_node(node.left, key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._add_node(node.right, key)
            else:
                node.right = Node(key)

    def add_node(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._add_node(self.root, key)

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


def build_tree_from_input(input_data):
    tree = BST()
    for key in input_data:
        tree.add_node(key)
    return tree

def get_height(nodes):
    tree = build_tree_from_input(nodes)
    return tree.height(tree.root)
def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline().strip())

        nodes = [list(map(int, input_file.readline().strip().split())) for _ in range(n)]
        result = get_height(nodes)
        output_file.write(str(result))

if __name__ == '__main__':
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
