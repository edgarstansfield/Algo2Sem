from utils import time, eigth_inp, eigth_out, time_and_memory

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

    nach = time.time()

    with open("../input.txt", "r", encoding='utf-8') as input_file, open("../output.txt", "w",
                                                                         encoding='utf-8') as output_file:
        for line in input_file:
            k, t, p = line.strip().split()
            result = k_mismatch_search(p, t, int(k))
            output_file.write(result)

    time_and_memory(nach)


if __name__ == '__main__':
    main()
