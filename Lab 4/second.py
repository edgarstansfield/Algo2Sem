import time

nach = time.time()

def tresure_map(s):
    s = ''.join(s.split())
    prev_char = {}
    my_l = [[0, 0] for _ in range(len(s))]

    for ind, char in enumerate(s):
        prev_i = prev_char.get(char, None)
        if prev_i is not None:
            my_l[ind][0] = my_l[prev_i][0] + 1
            my_l[ind][1] = my_l[prev_i][1] + my_l[prev_i][0] * (ind - prev_i) + (ind - prev_i - 1)
        else:
            my_l[ind] = [0, 0]
        prev_char[char] = ind

    total = sum(i[1] for i in my_l)
    return total


def main():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        s = input_file.read()
        result = tresure_map(s)
        output_file.write(str(result))


if __name__ == '__main__':
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)