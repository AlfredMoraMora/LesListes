# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_input = input(f'Enter the name of three students, separated by commas: ')
    student_names = user_input.split(',')
    print(student_names)
    student_names.sort()
    print(student_names)
    student_names.append("Daniel")
    print(student_names)
    student_names[0], student_names[3] = student_names[3], student_names[0]
    print(student_names)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
