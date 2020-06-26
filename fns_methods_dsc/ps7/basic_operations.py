def get_result(a, b, operation):
    # update operation_dict
    operation_dict = {'ADD': add, 'SUBTRACT': subtract, 'MULTIPLY': multiply, 'DIVIDE': divide}

    func = operation_dict[operation]

    result = func(a, b)

    print(result)


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b==0:
        print('Invalid input!')
    else:
        return a/b


numbers = input().split(",")
a,b=float(numbers[0]),float(numbers[1])
operation=input()

get_result(a, b, operation)