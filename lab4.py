# # 1)
# Sentence = "salem alem!"
# print (Sentence.title())

# # 2)
# Abc = "tODAY is February 9th. hello world"
# print(Abc.capitalize())

# # 3)
# Qwerty = " Today is february 9th "
# print(Qwerty.split())

# # 4)
# l1 = input('First line: ')
# l2 = input('Second line: ')
# print('Concatenated string =', l1 + l2)

# # 5)
# text = "Learning with Sololearn is easy."
# result = text.startswith('with', 9, 20)
# print(result)
# result = text.startswith('programming is', 7, 20)
# print(result)
# result = text.startswith('program', 7, 18)
# print(result)
# print(text[1:17])
# # 6)
# string = "MY DREAM IS TO BECOME A LA"
# print(string.swapcase())
# string = "my dream is to become a la"
# print(string.swapcase())
# string = "My DrEaM iS tO bEcOmE a La"
# print(string.swapcase())

# # 7)
# string = "THIS SHOULD BE LOWERCASE!"
# print(string.lower())
# # 8)
# random_string = '              this is good '
# print(random_string.lstrip())
# website = 'https://pythonstart.ru/'
# print(website.lstrip('ht'))
# # 9)
# string = "this should be uppercase!"
# print(string.upper())
# string = "This ShouLd Be uPpErCasE!"
# print(string.upper())

# # 10)
# string = ' xoxo love xoxo '
# print(string.strip())
# print(string.strip(' xoe'))
# print(string.strip('stx'))
# string = 'android is awesome'
# print(string.strip('an'))







# 2 zadanie

n = int(input())
names = [0] * n 
classes = [0] * n
temporaryName = ""
temporaryClass = 0

for i in range(len(names)):
    print("Enter surnames: " + str(i + 1))
    names[i] = str(input())
    print("Enter classes: " + str(i+1))
    classes[i] = int(input())

for i in range(len(classes) - 1):
    for j in range(len(classes) - 1):
        if classes[j] > classes[j + 1]:
            temporaryClass = classes[j + 1]
            classes[j + 1] = classes[j]
            classes[j] = temporaryClass
            temporaryName = names[j + 1]
            names[j + 1] = names[j]
            names[j] = temporaryName

for i in range(len(names)):
    print("Surname: " + names[i] + " Class: " + str(classes[i]))








# 3 zadanie

s = str("HeLLo World")
upperLet = int(0)
lowerLet = int(0)

for i in s:
    if i.islower() == True and i.isalpha() == True :
        lowerLet += 1
    elif i.isupper() == True and i.isalpha() == True :
        upperLet += 1
       
if upperLet > lowerLet:
    print(s.upper())
else:
    print(s.lower())
print(lowerLet)
print(upperLet)



n = input("Санды енгизиниз = ")

while (n.isdigit() == False):
    n = input("Кате, санды енгизиниз = ")

s = input("Санды енгизиниз = ")
while (s.isdigit() == False):
    s = input("Кате, санды енгизиниз = ")
print(int(n) + int(s))
