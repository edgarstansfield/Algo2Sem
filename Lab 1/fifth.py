import time
nach = time.time()

def main():

    def max_prize(n):
        n = n - 1
        sweets = [1]
        winner = 2
        while n > 0:
            if winner > n:
                sweets[-1] += n
                break
            else:
                sweets.append(winner)
                n -= winner
                winner += 1
        return sweets

    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                          encoding='utf-8') as output_file:
        n = int(input_file.readline())
        ans = [str(i) for i in max_prize(n)]
        output_file.write(f'{len(ans)}\n{" ".join(ans)}')

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)