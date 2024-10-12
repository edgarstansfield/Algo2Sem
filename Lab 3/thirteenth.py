import time

nach = time.time()

def main():
    def garden_count(graph):
        counter = 0

        for i in range(n):
            for j in range(m):
                if graph[i][j] == '#':
                    counter += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if graph[x][y] == '#':
                            graph[x][y] = '.'
                            if x > 0:
                                stack.append((x - 1, y))
                            if y > 0:
                                stack.append((x, y - 1))
                            if x < n - 1:
                                stack.append((x + 1, y))
                            if y < m - 1:
                                stack.append((x, y + 1))
        return counter


    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
        n, m = map(int, input_file.readline().split())
        garden = [list(input_file.readline().strip()) for _ in range(n)]
        output_file.write(str(garden_count(garden)))

if __name__ == "__main__":
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)