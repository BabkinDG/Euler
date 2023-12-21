#Наибольший простой множитель числа
number = 600851475143
factor = 1

while factor < number:
    factor += 1
    if (number % factor) == 0:
        number //= factor

print('Наибольшим простым множителем числа 600851475143 является ' + str(factor))