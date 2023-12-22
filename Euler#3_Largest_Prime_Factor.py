#Наибольший простой множитель числа
number = 600851475143
divider = 1

while divider < number:
    divider += 1
    if (number % divider) == 0:
        number //= divider

print('Наибольшим простым множителем числа 600851475143 является ' + str(divider))