a = [1,2,5,66,44,3,8]
for i in [1,2,5,66,44,3,8]:
   if i % 2 == 0:
       print(i)


a = int(input('введите минимальный элемент '))
b = int(input('введите максимальный элемент '))
summ = 0
for i in range(a+1,b):
    summ +=i
print(summ)




