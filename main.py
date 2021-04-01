# Exercise 4
def check_tables(table1, table2):
    tab = [i in table2 for i in list(map(lambda x: x**2, table1))]

    if len(tab) == set(table2):
        return True
    else:
        return False


# Exercise 2
# Number functions
def present_number(number, arg):
    if len(arg) is not 0:
        arg = arg[0] + [number]
    else:
        arg = [number]

    if len(arg) == 3:
        return arg[1](arg[0], arg[2])
    else:
        return arg


def one(*arg):
    return present_number(1, list(arg))


def two(*arg):
    return present_number(2, list(arg))


def three(*arg):
    return present_number(3, list(arg))


def four(*arg):
    return present_number(4, list(arg))


def fife(*arg):
    return present_number(5, list(arg))


def six(*arg):
    return present_number(6, list(arg))


def seven(*arg):
    return present_number(7, list(arg))


def eight(*arg):
    return present_number(8, list(arg))


def nine(*arg):
    return present_number(9, list(arg))


# Sign functions
def plus(*arg):
    arg = list(arg)
    if type(arg[0]) == int:
        return [arg[0]] + [lambda x, y: x + y]
    return arg[0] + [lambda x, y: x + y]



def minus(*arg):
    arg = list(arg)
    if type(arg[0]) == int:
        return [arg[0]] + [lambda x, y: y - x]
    return arg[0] + [lambda x, y: y - x]


def divided_by(*arg):
    arg = list(arg)
    if type(arg[0]) == int:
        return [arg[0]] + [lambda x, y: y // x]
    return arg[0] + [lambda x, y: y // x]


def times(*arg):
    arg = list(arg)
    if type(arg[0]) == int:
        return [arg[0]] + [lambda x, y: x * y]
    return arg[0] + [lambda x, y: x * y]


if __name__ == '__main__':

    print(f"wynik {eight(plus(two()))}")
    print(f"wynik {eight(times(three()))}")
    print(f"wynik {eight(divided_by(three()))}")
    print(f"wynik {eight(minus(six(divided_by(three()))))}")
    print(check_tables([121, 144, 19, 161, 144, 19, 11], [121, 14641, 20736, 362, 25921, 362, 20736, 361]))


