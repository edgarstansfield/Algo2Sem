import time
nach = time.time()

def main():

    def min_ref(x, y, z, n):
        x = [0] + x + [y]

        refuel = 0
        curr = 0
        while curr <= n:
            last_refill = curr

            while curr <= n and x[curr + 1] - x[last_refill] <= z:
                curr += 1

            if last_refill == curr:
                return -1

            if curr <= n:
                refuel += 1

        return refuel



    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                          encoding='utf-8') as output_file:
        y, z, n = int(input_file.readline()), int(input_file.readline()), int(input_file.readline())
        stop = [int(i) for i in input_file.readline().split()]
        output_file.write(str(min_ref(stop, y, z, n)))

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
