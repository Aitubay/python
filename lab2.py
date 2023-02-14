# 2 - тапсырма

n = int(input("n = "))
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1

# 2 - тапсырма

res = 1
n = int(input("n = "))
for i in range(1, n + 1):
    res *= i
print(res)

# 3 - тапсырма (1)

langs = ["Python", "Java", "JS", "Kotlin"]
enumNames = enumerate(langs, 1)
print(list(enumNames))

# 4 - тапсырма (1)
import random

massive=[]
n=int(input("n = "))
for i in range(1, n+1):massive.append(random.randint(1,10))
print(massive)