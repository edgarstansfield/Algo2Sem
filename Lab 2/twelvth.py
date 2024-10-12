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

    def add_node(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add_node(self.root, key)

    def _add_node(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._add_node(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._add_node(node.right, key)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        return right_height - left_height


def build_tree_from_list(node_list):
    tree = BST()
    for key in node_list:
        tree.add_node(key)
    return tree


def get_balances(tree):
    balances = []
    queue = [tree.root]
    while queue:
        node = queue.pop(0)
        balances.append(tree.balance(node))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return balances


def main():
    with open("input.txt", "r") as in_file, open("output.txt", "w") as out_file:
        n = int(in_file.readline())

        if n == 0:
            out_file.write(str(0))
        else:
            nodes = [int(in_file.readline().split()[0]) for _ in range(n)]

            tree = build_tree_from_list(nodes)

            balances = get_balances(tree)
            for bl in balances:
                out_file.write(f"{bl}\n")


if __name__ == '__main__':
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)