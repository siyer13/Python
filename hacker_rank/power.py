if __name__ == '__main__':
    n = int(input())
    ls = [ str(i**2) for i in range(n)]
    print('\n'.join(ls))
    print(4/3)
    print(int(4/3))


    def is_leap(year):
        leap = False

        # Write your logic here
        if year / 4 == 0:
            if year / 100 == 0:
                if year / 400 == 0:
                    leap = True
        return leap


    year = int(input())
    print(is_leap(year))
