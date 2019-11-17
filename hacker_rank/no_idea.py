# https://www.hackerrank.com/challenges/no-idea/problem


if __name__ == '__main__':

    print('Enter range: ')
    n, m = input().split()
    n = int(n)
    m = int(m)
    happiness = 0
    print('Enter array values: ')
    ar_val = [input() for i in range(n)]
    print('Enter Set-A values: ')
    set_a = set([input() for i in range(m)])
    print('Enter Set-B values: ')
    set_b = set([input() for i in range(m)])

    print('Array: %s ' % str(ar_val))
    print('Set A: %s ' % str(set_a))
    print('Set B: %s ' % str(set_b))

    happiness = sum([(i in set_a) - (i in set_b) for i in ar_val])

    print('Happiness: %s ' % str(happiness))

