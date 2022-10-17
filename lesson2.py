a = [1,2,5,66,44,3,8]
for i in [1,2,5,66,44,3,8]:
   if i % 2 == 0:
       print(i)

for i in range(1,11):#вывести диапазон 1-10, кроме 5
    if i == 5:
        continue
    print(i)

for i in range (10,20): #диапазон 10-20, прерывается на 15
    if i == 15+1:
        break
    print(i)

a = int(input('введите минимальный элемент '))
b = int(input('введите максимальный элемент '))
summ = 0
for i in range(a+1,b):
    summ +=i
print(summ)




