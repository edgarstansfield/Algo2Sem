import time
nach = time.time()
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.inserting(self.root, key)

    def inserting(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self.inserting(root.left, key)
        elif key > root.val:
            if root.right is None:
                root.right = Node(key)
            else:
                self.inserting(root.right, key)

    def finding(self, root, key, min_greater):
        if root is None:
            return 0 if min_greater == float('inf') else min_greater
        if root.val > key:
            min_greater = min(min_greater, root.val)
            return self.finding(root.left, key, min_greater)
        else:
            return self.finding(root.right, key, min_greater)

    def find_min(self, key):
        return self.finding(self.root, key, float('inf'))

def process_commands(commands):
    bst = BST()
    result = []
    for command in commands:
        if command.startswith('+'):
            _, x = command.split()
            bst.insert(int(x))
        elif command.startswith('>'):
            _, x = command.split()
            result.append(bst.find_min(int(x)))
    return result

def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
        commands = input_file.readlines()
        result = process_commands(commands)
        for elem in result:
            output_file.write(f'{elem}\n')

if __name__ == '__main__':
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)