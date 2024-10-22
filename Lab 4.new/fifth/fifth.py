from utils import time, fifth_inp, fifth_out, time_and_memory

def prefix_function(s):
    j = 0
    prefix = [0] * len(s)
    for i in range(1, len(s)):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix


def main():

    nach = time.time()

    s = fifth_inp()
    result = prefix_function(s)
    fifth_out(result)

    time_and_memory(nach)



if __name__ == '__main__':
    main()
