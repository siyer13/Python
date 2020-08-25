import functools

if __name__ == '__main__':
    n = int(input())
    
    arr = set(list(map(int, input().split())))
    
    max = functools.reduce(lambda a,b: a if a > b else b, arr)

    arr.remove(max)

    max = functools.reduce(lambda a,b: a if a > b else b, arr)

    print(max)
