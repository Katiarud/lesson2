for i in range (10,20): #диапазон 10-20, прерывается на 15
    if i < 16:
        print(i)

for i in range(1,11):#вывести диапазон 1-10, кроме 5
    if i % 5 != 0: # вопрос--- 10 у меня тоже не вывелось, подскажите как сделать?
        print(i)
print("*************************")

for i in range(6,19): # вывести нечетные числа
    if i % 2 == 1:
        print(i)

for i in range(33,99): # вывести числа кратные 2
    if i % 2 == 0:
        print(i)

for i in range(60,101): # вывести диапазон чисел
    print(i)

a1 = input("введите  натуральное чисело: ") # найти сумму и разность чисел
a2 = input("введите  натуральное чисело: ")
s = int(a1) + int(a2)
r = int(a1) - int(a2)
print(s, r)

a = [1,2,3,4] # вывести первое и последнее значение
print(a[0], a[-1])

chislo = input("введите пятизначное натуральное чисело: ")
a = int(chislo[0])
b = int(chislo[1])
c = int(chislo[2])
d = int(chislo[3])
f = int(chislo[4])
for i in [a, b, c, d, f]:
    for j in range(1,9):
       if i % j != 0:
            print (i, "максимальная цифра в вашем чисте")





