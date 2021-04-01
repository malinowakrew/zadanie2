# Exercise 2
# Number functions
def present_number(number, arg):
    try:
        if len(arg) is not 0:
            arg = arg[0] + [number]
        else:
            arg = [number]

        if len(arg) == 3:
            return arg[1](arg[0], arg[2])
        else:
            return arg
    except Exception as error:
        print(f"error: {error}")
        return []


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

def equation(arg, lambda_equation):
    try:
        if type(arg[0]) == int:
            return [arg[0]] + [lambda_equation]
        return arg[0] + [lambda_equation]

    except Exception as error:
        print(f"error: {error}")
        return []


def plus(*arg):
    return equation(list(arg), lambda x, y: x + y)


def minus(*arg):
    return equation(list(arg), lambda x, y: y - x)


def divided_by(*arg):
    return equation(list(arg), lambda x, y: y // x)


def times(*arg):
    return equation(list(arg), lambda x, y: x * y)


if __name__ == '__main__':

    print(f"8 + 2 =  {eight(plus(two()))}")
    print(f"8 * 3 = {eight(times(three()))}")
    print(f"8 / 3 = {eight(divided_by(three()))}")
    print(f"8 * (6 / (4 / 2)) = {eight(times(six(divided_by(four(divided_by(two()))))))}")


