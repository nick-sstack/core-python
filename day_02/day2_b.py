# 1
l = [3, "word", 3.14]
print(l)

# 2
l = [1, 1, [1, 2]]
print(l[2][1])

# 3
lst = ["a", "b", "c"]
print(lst[1:])  # ['b', 'c']

# 4
print(
    {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7,
    }
)

# 5
D = {"k1": [1, 2, 3]}
print(D["k1"][1])  # 2

# 6
l = [1, [2, 3]]
print(tuple(l))

# 7
print("\n#4")
m = "mississippi"
chars = set()
word = ""
for l in m:
    if l not in chars:
        chars.add(l)
        word += l
print(word)

# 8
chars.add("X")

# 9
print(set([1, 1, 2, 3]))  # {1, 2, 3}

ans = ""
for num in range(2000, 3201):
    if not num % 7 and num % 5:
        ans += str(num) + ","
print(ans)


def fact(num):
    if num == 0:
        return 1
    return num * fact(num)


n = 5
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print(d)

values = "1,4,6,32,7,2"
l = values.split(",")
t = tuple(l)
print(l)
print(t)


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())
