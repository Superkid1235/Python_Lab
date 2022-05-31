def is_odd(var_1):
    if var_1 % 2 != 0:
        # print(f"{var_1} is ODD")
        return True
    else:
        return False


def some_function():
    i = 0
    while i <= 10:
        if is_odd(i):
            print(f"{i} = ODD")
        else:
            print(f"{i} = EVEN")
        i += 1

def just_function():
    return "a", 30

def add_student(name, age, score):
    student_DB.append([name,age,score])


student_DB = []

add_student("James",22,57)
print(student_DB[0])

add_student("Marry Ann",25,82)
print(student_DB[1])