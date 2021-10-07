# 1
a = 20 + 20
print(a)

# 2
print(30 + 6)
print(30 * 6)
print(6 ** 6)
print(6 + 6 + 6 + 6 + 6 + 6)

# 3
print("Hello World")
print("Hello World : 10")
print("Hello World\n" * 10)

# 4
p = 800000
r = 0.06
m = 10000

i = 0
while p > 0:
    p = (p + (p * (r / 12))) - m
    i += 1

print("%d months" % i)
