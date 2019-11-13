# https://www.hackerrank.com/challenges/swap-case/problem


# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

def swap_case(str):
    s = list(str)
    i = 0
    for e in s:
        if e.isupper():
            s[i] = e.lower()
        elif e.islower():
            s[i] = e.upper()
        i = i+1
    str = "".join(s)
    return str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

