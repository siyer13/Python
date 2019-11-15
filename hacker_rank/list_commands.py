# https://www.hackerrank.com/challenges/python-lists/problem

my_list = []


def insert(lst, a, e):
    i = int(a)
    lst.insert(i, e)
    return lst


def append(lst, e):
    lst.append(e)
    return lst


def sort(lst):
    lst.sort()
    return lst


def print_list(lst):
    print(lst)


def remove(lst, e):
    lst.remove(e)
    return lst


def pop(lst):
    lst.pop()
    return lst


def reverse(lst):
    lst.reverse()
    return lst


if __name__ == '__main__':
    print("Enter range of commands: ")
    n = int(input())
    commands = []
    for i in range(n):
        print("Enter command :")
        cmd = input()
        commands.append(cmd)
    print("List of Commands", str(commands))
    for c in commands:
        if 'insert' in c:
            cmds = c.split(" ")
            my_list = insert(my_list, cmds[1], cmds[2])
        elif 'remove' in c:
            cmds = c.split(" ")
            my_list = remove(my_list, cmds[1])
        elif 'append' in c:
            cmds = c.split(" ")
            my_list = append(my_list, cmds[1])
        elif 'sort' in c:
            my_list = sort(my_list)
        elif 'pop' in c:
            my_list = pop(my_list)
        elif 'reverse' in c:
            my_list = reverse(my_list)
        elif 'print' in c:
            print_list(my_list)
        else:
            print("Not a List command")
