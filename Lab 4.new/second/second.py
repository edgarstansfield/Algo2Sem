from utils import time, sec_inp, sec_out, time_and_memory

def function(s):
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

    nach = time.time()

    s = sec_inp()
    result = function(s)
    sec_out(result)

    time_and_memory(nach)

if __name__ == '__main__':
    main()
