#Сумма чисел кратных 3 или 5 от 0 до 1000-1
summ = 0
number = 0

while number < 1000-1:
    number += 1
    if (number % 3) == 0 or (number % 5) == 0:
        summ += number

print('Сумма чисел кратных 3 или 5 от 0 до 1000 равна ' + str(summ))