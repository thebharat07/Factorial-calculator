import functools
x = input("Enter the number : ")


def numbers(x):
    i = 0
    result_list = []
    while i < int(x):
        i = i+1
        result_list.append(i)
    return result_list


if int(x) == 0:
    print(1)
else:

    try:
        n = functools.reduce(lambda x, y: x*y, numbers(x))
    except ValueError as e:
        print("Enter numbers only!")
    else:
        print(int(x), "! = ", n)