a = [2,0,48,27,36,-41,7,1]
n = sum(a) / len(a)
print(int(n))
for i in a:
    if i < n:
        print(i)

print('------------------')

n = [1,5,-6,-9,7,8,2]
summ = 0
for i in n:
    if i >0 and i %2 == 0:
        summ += i
print(summ)

               

print('---------------')

import random
n = random.randint(1000000000,9999999999)
print(n)
summ = 0
for i in str(n):
    summ +=int(i)
print(summ)



