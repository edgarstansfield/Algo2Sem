import time
nach = time.time()

def main():

    with open("input.txt", "r") as file:
        n = int(file.readline())
        values = list(map(int, file.readline().split()))

    total = sum(values)

    if total % 3 != 0:
        result = 0
    else:
        target = total // 3
        matr = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            matr[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if values[i - 1] <= j:
                    matr[i][j] = matr[i - 1][j] or matr[i - 1][j - values[i -1]]
                else:
                    matr[i][j] = matr[i - 1][j]
        result = 1 if matr[n][target] else 0
    with open("output.txt", "w") as file:
        file.write(str(result))

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)