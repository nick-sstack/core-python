# 1
def list_range():
    l = list()
    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            l.append(num)
    print(l)


# list_range()

# 2
def convert(num, u="f"):
    if u == "f":
        return (num - 32) * 5 / 9
    elif u == "c":
        return (num * 9 / 5) + 32
    else:
        return None


# print("43f is %1.2fc" % convert(43))

# 3
import random


def guess_random():
    rand = random.randint(1, 9)
    guess = 0
    while guess != rand:
        guess = int(input("Enter guess between 1 and 9: "))
        if guess < rand:
            print("Too low")
        elif guess > rand:
            print("Too high")
        else:
            print("Correct!")


# guess_random()

# 4 5
def print_pattern():
    for i in range(10):
        num = i
        if num > 5:
            num = 10 - num

        for j in range(num):
            print("*", end="")
        print()


# 6
def reverse_user():
    inp = input("Enter input: ")
    print(inp[::-1])


# reverse_user()

# 7
def count_odd_and_even():
    l = [3, 4, 5, 3, 2, 1, 6, 7, 4, 2, 1, 3]
    odds = 0
    evens = 0
    for num in l:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("Odds: %d, Evens: %d" % (odds, evens))


# count_odd_and_even()

# 8
def print_type():
    l = [23, True, 54.22, "string", [3, 2], {"one"}, {"one": 1}]
    for i in l:
        print("%s: %s" % (str(i), type(i)))


# print_type()

# 9
def print_not_3_or_6():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        else:
            print(i)


# print_not_3_or_6()
