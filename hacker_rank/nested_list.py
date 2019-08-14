if __name__ == '__main__':
    students = []
    lowest = 0.0
    highest = 0.0
    second_lowest = 0.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_mark_list = []
        name_mark_list.append(name)
        name_mark_list.append(score)
        if lowest == 0.0:
            students.append(name_mark_list)
            lowest, highest, second_lowest = score
        elif lowest == score:
            students.append(name_mark_list)
        elif lowest > score:
            students.clear()
            lowest = score
            students.append(name_mark_list)

    print(students)
    stu_name = []
    for student in students:
        stu_name.append(student[0])
    for name in sorted(stu_name):
        print(name)


