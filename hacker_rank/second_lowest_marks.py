# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]
    second_lowest_mark = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_lowest_mark]))
