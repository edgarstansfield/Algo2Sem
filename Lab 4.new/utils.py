import time
import os
import psutil


def time_and_memory(n):
    kon = time.time()
    c = kon - n
    print('Время :', c)
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

def sec_inp():
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        s = input_file.read()
        return s


def sec_out(res):
    with open("output.txt", "w",encoding='utf-8') as output_file:
        output_file.write(str(res))

def ninth_inp():
    with open('input.txt', 'r') as file:
        s = file.readline().strip()
    return s

def ninth_out(res):
    with open('output.txt', 'w') as file:
        file.write(res + '\n')

def fifth_inp():
    with open("input.txt", "r", encoding='utf-8') as input_file:
        s = input_file.readline().strip()
        return s

def fifth_out(res):
    with open("output.txt", "w", encoding='utf-8') as output_file:
        output_file.write(' '.join(map(str, res)))

def eigth_inp():
    with open("input.txt", "r", encoding='utf-8') as input_file:
        return input_file.read()

def eigth_out(res):
    with open("output.txt", "w", encoding='utf-8') as output_file:
        output_file.write(res)






