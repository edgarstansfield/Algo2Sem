import time
nach = time.time()

def main():

    def count_palindromic_substrings(length, max_changes, string):
        total_palindromes = 0

        def check_palindromes(center, even_length=False):
            nonlocal total_palindromes
            changes_made = 0
            for offset in range(1, length):
                if even_length:
                    left_idx = center - offset + 1
                    right_idx = center + offset
                else:
                    left_idx = center - offset
                    right_idx = center + offset

                if left_idx < 0 or right_idx >= length:
                    break
                if string[left_idx] != string[right_idx]:
                    if changes_made != max_changes:
                        total_palindromes += 1
                        changes_made += 1
                    else:
                        break
                else:
                    total_palindromes += 1

        for center in range(length):
            total_palindromes += 1
            check_palindromes(center)
            check_palindromes(center, True)

        return total_palindromes


    with open("input.txt", "r") as file:
        length, max_changes = map(int, file.readline().split(" "))
        string = file.readline().strip()

    res = count_palindromic_substrings(length, max_changes, string)

    with open('output.txt', 'w') as file:
        file.write(str(res))

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
