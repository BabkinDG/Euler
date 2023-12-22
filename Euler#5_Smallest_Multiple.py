#Самое маленькое число, которое делится нацело на все числа от 1 до 20
number = 0
int_div = 0
answer = False

while answer == False:
    number += 20
    for factor in range(1, 21):
         if number % factor == 0:
            int_div += 1
            if int_div == 20:
                answer = True
         else:
            int_div = 0
            break

print('Самым маленьким числом, которое делится нацело на все числа от 1 до 20 является ' + str(number))