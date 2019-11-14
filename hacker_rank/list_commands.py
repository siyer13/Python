# https://www.hackerrank.com/challenges/python-lists/problem

my_list = []


def insert(lst, a, e):
    i = int(a)
    print('E', e)
    lst.insert(i, e)
    print("lIST", str(lst))
    return lst


def print_list(lst):
    print(lst)


def remove(lst, e):
    lst.remove(int(e))
    return lst


if __name__ == '__main__':
    print("Enter range of commands: ")
    n = int(input())
    commands = []
    for i in range(n):
        print("HARI is a very good boy: ")
        cmd = input()
        commands.append(cmd)
    print("List of Commands", str(commands))
    for c in commands:
        print("cmds : ", str(c))
        if 'insert' in c:
            print('Inside insert: ')
            print(c)
            cmds = c.split(" ")
            print(cmds)
            print(cmds[1], cmds[2])
            my_list = insert(my_list, cmds[1], cmds[2])
            print("Mylist", str(my_list))
        elif 'print' in c:
            print(my_list)
        elif 'remove' in c:
            cmds = c.split(" ")
            remove(my_list, cmds[1])
