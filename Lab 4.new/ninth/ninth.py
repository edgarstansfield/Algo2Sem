from utils import time, ninth_inp, ninth_out, time_and_memory


def encode_string(s):
    n = len(s)
    dp = [["" for _ in range(n)] for _ in range(n)]

    for l in range(n):
        for i in range(n - l):
            j = i + l
            substr = s[i:j + 1]
            dp[i][j] = substr

            if j - i < 4:
                continue

            for k in range(i, j):
                if len(dp[i][j]) > len(dp[i][k] + '+' + dp[k + 1][j]):
                    dp[i][j] = dp[i][k] + '+' + dp[k + 1][j]

            for k in range(1, len(substr)):
                repeat_str = substr[:k]
                if repeat_str and len(substr) % len(repeat_str) == 0 and substr == repeat_str * (
                        len(substr) // len(repeat_str)):
                    encoded = f"{dp[i][i + k - 1]}*{len(substr) // len(repeat_str)}"
                    if len(encoded) < len(dp[i][j]):
                        dp[i][j] = encoded

    return dp[0][n - 1]


def main():

    nach = time.time()

    s = ninth_inp()
    result = encode_string(s)
    ninth_out(result)

    time_and_memory(nach)

if __name__ == "__main__":
    main()
