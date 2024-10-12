import time

nach = time.time()
def k_mismatch_search(p, t, k):
    matches = []

    for i in range(len(t) - len(p) + 1):
        mismatches = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                mismatches += 1
                if mismatches > k:
                    break
        if mismatches <= k:
            matches.append(i)
    ans = f'{len(matches)} {" ".join(map(str, matches))}\n'
    return ans


def main():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        for line in input_file:
            k, t, p = line.strip().split()
            result = k_mismatch_search(p, t, int(k))
            output_file.write(result)


if __name__ == '__main__':
    main()

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)