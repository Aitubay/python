def sortSur(nameList):
    l2 = []

    for ele in nameList:
        l2.append(ele.split())
    nameList = []

    for ele in sorted(l2, key=lambda x: x[-1]):
        nameList.append(' '.join(ele))

    return nameList


nameList = ['Arapova Assylzhan Class 5', 'Bolatbek Aigerim Class 1', 'Adil Uldana Class 4', 'Asylbekova Aiymgul Class 8',
            'Tazhieva Symbat Class 9']

print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))



# 2 zadanie
spisok = {
    "Assylzhan": (70,80,70),
    "Aigerim": (65,60,70,80),
    "Uldana": (90,50,70),
    "Aiymgul": (90,70,65),
    "Symbat": (70,85,65,90),
    "Zhanyl":(65,85,90,100)}


spi = sorted(spisok.items(), key=lambda spisok: spisok[0])
print(spi)

name = str(input("Name: "))
for key in spisok:
    if key == name:
        print(spisok[key])



# 3 zadanie

arr = []
san = 1
while san!=0:
    san = int(input("San jaz: "))
    if san !=0:
        arr.append(san)
    
arr.sort()
print("Sort po vozrastaniu: ")
for i in range(len(arr)):
    print(arr[i])

print("Sort po ubivaniu: ")
for i in range(len(arr)):
    print(arr[len(arr)-i-1])



# 4 zadanie
import random
ran = []
j = 0
while j!=6:
    daf = True
    rand = random.randint(1,50)
    for i in range(len(ran)-1):
        san1 = ran[i+1]
        if ran[i] == san1:
            daf = False 

    if daf:
        ran.append(rand)
        j+=1

ran.sort()
print(ran)


#5

a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [1,2,5,6,3]
def sortedList(l):
    l1 = sorted(l)
    l2 = sorted(l, reverse = True)
    return (l == l1) or (l == l2)
print(sortedList(a))
print(sortedList(b))
print(sortedList(c))