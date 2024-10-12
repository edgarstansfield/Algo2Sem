import time
nach = time.time()

def main():

    def max_num(n, arr):
        for i in range(n - 1):
            for j in range(n - i - 1):
                v1 = arr[j] + arr[j + 1]
                v2 = arr[j + 1] + arr[j]
                if v1 < v2:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return "".join(arr)
    with open("input.txt", "r") as file:
        n = int(file.readline())
        arr = list(file.readline().split())
    with open("output.txt", "w") as file:
        file.write(str(max_num(n, arr)))

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)