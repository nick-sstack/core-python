# 1
print("#1")
print("Hello World"[8])

# 2
print("\n#2")
print("thinker"[2:5])
s = "hello"
print(s[1])  # e

# 3
print("\n#3")
s = "Sammy"
print(s[2:])  # mmy

# 4
print("\n#4")
m = "mississippi"
chars = set()
word = ""
for l in m:
    if l not in chars:
        chars.add(l)
        word += l
print(word)

# 5
print("\n#5")
str1 = "Amore, Roma"
str2 = "No 'x' in Nixon"
str3 = "Was it a cat I saw?"

word = ""
for l in str3:
    if l.isalpha():
        word += l.lower()

print(word)
print(word == word[::-1])
