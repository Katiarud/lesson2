chis = int(input("введите минимальное натуральное чисело: "))
chis2 = int(input("введите максимальное натуральное чисело: "))
i = int(input("введите шаг"))
print(int((chis2 - chis) % i))  # количество шагов
if chis > 0 and chis2 > chis:
    a = str(chis + i)
    b = str(chis + i*2)
    c = str(chis + i*3)
    d = str(chis + i*4)
    e = str(chis + i*5)
    f = str(chis + i*6)
    print(a,b,c,d,e,f)
else:
   print("число введено не верно")














