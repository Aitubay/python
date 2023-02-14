
#4 - тапсырма (1)
# a = int(input("A = "))
# b = int(input("B = "))

# for i in range(a, b + 1):
#     print(i)
#(2)

# a = int(input("A = "))
# b = int(input("B = "))
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)

# # (3)
# a = int(input("A = "))
# b = int(input("B = "))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')

# (4)
n = int(input("N = "))
sum = 0
for i in range(n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print("x = ", sum)