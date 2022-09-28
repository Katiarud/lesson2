try :
    man1 = input("введите год, номер месяца и день рождения первого человека")
    man2 = input("введите год, номер месяца и день рождения второго человека")
    if int(man1[0:4:1]) < int(man2[0:4:1]):
        print("первый старше второго")
    elif int(man1[0:4:1]) > int(man2[0:4:1]):
        print("второй старше первого")
    elif int(man1[0:4:1]) == int(man2[0:4:1]) and int(man1[4:6:1]) > int(man2[4:6:1]):
        print("второй старше первого")
    elif int(man1[0:4:1]) == int(man2[0:4:1]) and int(man1[4:6:1]) < int(man2[4:6:1]):
        print("первый старше второго")
    elif int(man1[0:6:1]) == int(man2[0:6:1]) and int(man1[-2] + man1[-1]) > int(man2[-2] + man2[-1]):
        print("второй старше первого")
    else:
        print("первый старше второго")
except ValueError:
    print("введите только числа начиная с года")














