import time
nach = time.time()

def main():
    def maxExpressionValue(expression):
        def findMinAndMax(start, end, maxValues, minValues, operators):
            current_min = float("inf")
            current_max = float("-inf")
            for index in range(start, end):
                a = eval(f"{maxValues[start][index]} {operators[index]} {maxValues[index + 1][end]}")
                b = eval(f"{maxValues[start][index]} {operators[index]} {minValues[index + 1][end]}")
                c = eval(f"{minValues[start][index]} {operators[index]} {maxValues[index + 1][end]}")
                d = eval(f"{minValues[start][index]} {operators[index]} {minValues[index + 1][end]}")
                current_min = min(current_min, a, b, c, d)
                current_max = max(current_max, a, b, c, d)
            return current_min, current_max

        digits = list(map(int, expression[::2]))
        operators = list(expression[1::2])
        length = len(digits)
        minValues = [[0] * length for _ in range(length)]
        maxValues = [[0] * length for _ in range(length)]

        for i in range(length):
            minValues[i][i] = digits[i]
            maxValues[i][i] = digits[i]

        for s in range(1, length):
            for start in range(length - s):
                end = start + s
                minValues[start][end], maxValues[start][end] = findMinAndMax(start, end, maxValues, minValues, operators)

        return maxValues[0][length - 1]




    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                          encoding='utf-8') as output_file:
        s = input_file.read().rstrip()
        res = maxExpressionValue(s)
        output_file.write(str(res))

kon = time.time()
c = kon - nach
print('Время :', c)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)