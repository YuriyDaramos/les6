
def sum(a, b):
    return a + b


def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

#
# def log_error(*args):
#     print("operator not exist")


OPERATORS = {
    "+": sum,
    "-": minus,
    "*": mul
}

EXIT_COMMAND = "\q"
CLEAR_COMMAND = "\c"
# tetettet
ERROR_MSG_INVALID_DATA = "Invalid data"

a = None
operator = None
b = None


while True:
    if a is None:
        a = input("Input a: ")
        if a == EXIT_COMMAND:
            break
        elif a == CLEAR_COMMAND:
            a = None
            operator = None
            b = None
            continue

        try:
            a = float(a)
        except ValueError:
            print(ERROR_MSG_INVALID_DATA)
            a = None
            continue

    if operator is None:
        operator = input("Input operator: ")
        if operator == EXIT_COMMAND:
            break
        elif operator == CLEAR_COMMAND:
            a = None
            operator = None
            b = None
            continue

        if operator not in OPERATORS:
            print(ERROR_MSG_INVALID_DATA)
            operator = None
            continue

    if b is None:
        b = input("Input b: ")
        if b == EXIT_COMMAND:
            break
        elif b == CLEAR_COMMAND:
            a = None
            operator = None
            b = None
            continue

        try:
            b = float(b)
        except ValueError:
            print(ERROR_MSG_INVALID_DATA)
            b = None
            continue

    operator_method = OPERATORS.get(operator)

    result = operator_method(a, b)
    a = result
    operator = None
    b = None
    print(result)
