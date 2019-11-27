if __name__ == '__main__':
    students = []
    lowest = 0.0
    highest = 0.0
    second_lowest = 0.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_mark_list = [name, score]
        if lowest == 0.0:
            students.append(name_mark_list)
            lowest = score
            second_lowest = score
            highest = score
        elif second_lowest == score:
            students.append(name_mark_list)
        elif score > highest:
            highest = score
        elif lowest < score < highest:
            second_lowest = score
        elif lowest < score:
            lowest = score
            students.clear()
            students.append(name_mark_list)

    print(lowest)
    print(second_lowest)
    print(highest)
    print(students)
    stu_name = []
    for student in students:
        stu_name.append(student[0])
    for name in sorted(stu_name):
        print(name)


