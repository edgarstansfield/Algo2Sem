import time
nach = time.time()

def main():


    def dark_knight(n):
        motion = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        mod = 10 ** 9
        for i in range(n - 1):
            motion = [
                (motion[4] + motion[6]) % mod,
                (motion[6] + motion[8]) % mod,
                (motion[7] + motion[9]) % mod,
                (motion[4] + motion[8]) % mod,
                (motion[0] + motion[3] + motion[9]) % mod,
                0,
                (motion[0] + motion[1] + motion[7]) % mod,
                (motion[2] + motion[6]) % mod,
                (motion[1] + motion[3]) % mod,
                (motion[2] + motion[4]) % mod
            ]
        return sum(motion) % mod



    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline())
        result = dark_knight(n)
        output_file.write(str(result))

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)