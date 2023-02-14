

s = str("HeLLo World")
upperLet = int(0)
lowerLet = int(0)

for i in range(len(s)):
    if s[i].islower() == True and s[i].isalpha() == True :
        lowerLet += 1
    elif s[i].isupper() == True and s[i].isalpha() == True :
        upperLet += 1
       
if upperLet > lowerLet:
    print(s.upper())
else:
    print(s.lower())
print(lowerLet)
print(upperLet)



# n = input("Санды енгизиниз = ")

# while (n.isdigit() == False):
#     n = input("Кате, санды енгизиниз = ")

# s = input("Санды енгизиниз = ")
# while (s.isdigit() == False):
#     s = input("Кате, санды енгизиниз = ")
# print(int(n) + int(s))
