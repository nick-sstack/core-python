# 1
def func():
    print("Hello World")


# 2
def func1(name):
    print("Hello my name is %s" % name)


# 3
def func3(x, y, z):
    if z:
        return x
    else:
        return y


# 4
def func4(x, y):
    return x * y


# 5
def is_even(x):
    return x % 2 == 0


# 6
def is_greater(x, y):
    return x > y


# 7
def arb_args(*args):
    return sum(args)


# print(arb_args(4, 6, 2, 1, 2, 3, 4))

# 8
def even_args(*args):
    return [x for x in args if x % 2 == 0]


# print(even_args(2, 4, 5, 2, 1, 23, 5, 4, 2, 2))

# 9
def even_odd_string(s):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


# print(even_odd_string("dkfjwojdsf"))

# 10
def lesser_if_even(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return x if x < y else y
    else:
        return x if x > y else y


# print(lesser_if_even(8, 6))

# 11
def comp_first_letter(s1, s2):
    return s1[0] == s2[0]


# print(comp_first_letter("djslfkj", "edjfsl"))

# 12
def num_seven(num):
    val = (abs(num - 7)) * 2
    return 7 + val if num < 7 else 7 - val


# print(num_seven(10))

# 13
def cap_first_fourth(s):
    return "".join([c.upper() if i == 0 or i == 3 else c for i, c in enumerate(s)])


# print(cap_first_fourth("dskfjljiwei"))
