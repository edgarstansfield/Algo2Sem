import time
nach = time.time()

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

        self.size = 1


class BST:
    def __init__(self):
        self.root = None

    def get_size(self, node):
        if node is None:
            return 0
        return node.size

    def _inserting(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                root.left = self._inserting(root.left, key)
        elif key > root.val:
            if root.right is None:
                root.right = Node(key)
            else:
                root.right = self._inserting(root.right, key)
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        return root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._inserting(self.root, key)

    def _min_val_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_node(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete_node(root.left, key)
        elif key > root.val:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_val_node(root.right)
            root.val = temp.val
            root.right = self._delete_node(root.right, temp.val)
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        return root

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _find_k_max(self, root, k):
        if root is None:
            return None
        right_size = self.get_size(root.right)
        if right_size + 1 == k:
            return root.val
        elif k <= right_size:
            return self._find_k_max(root.right, k)
        else:
            return self._find_k_max(root.left, k - right_size - 1)

    def find_k_max(self, k):
        return self._find_k_max(self.root, k)


def process_commands(operations):
    bst = BST()
    ans = []
    for line in operations:
        if line.startswith('+1'):
            _, x = line.split()
            bst.insert(int(x))
        elif line.startswith('-1'):
            _, x = line.split()
            bst.delete(int(x))
        elif line.startswith('0'):
            _, x = line.split()
            result = bst.find_k_max(int(x))
            if result is not None:
                ans.append(result)

    return ans


def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline().strip())
        commands = input_file.readlines()
        ans = process_commands(commands)
        for elem in ans:
            output_file.write(f'{elem}\n')


if __name__ == '__main__':
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)