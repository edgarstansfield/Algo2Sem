import time

nach = time.time()


def main():
    def has_negative_cycle(graph, n):
        distances = [float('inf')] * n
        distances[0] = 0

        for _ in range(n - 1):
            for u in range(n):
                for v, weight in graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        for u in range(n):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    return 1

        return 0

    with open("input.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, weight = map(int, file.readline().split())
            graph[u - 1].append((v - 1, weight))

    result = has_negative_cycle(graph, n)
    with open("output.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)