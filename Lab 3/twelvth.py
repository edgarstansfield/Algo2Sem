import time

nach = time.time()

def main():
    def labyrinth(graph, colors):
        node = 1
        for color in colors:
            if color in graph[node]:
                node = graph[node][color]
            else:
                return 'INCORRECT'
        return node


    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
        n, m = map(int, input_file.readline().split())
        graph = {i: {} for i in range(1, n + 1)}

        for _ in range(m):
            u, v, c = map(int, input_file.readline().split())
            graph[u][c] = v
            graph[v][c] = u


        input_file.readline()

        colors = [int(i) for i in input_file.readline().split()]

        output_file.write(str(labyrinth(graph, colors)))

if __name__ == "__main__":
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)