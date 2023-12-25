#Самое маленькое число, которое делится нацело на все числа от 1 до 20
number = 0
int_div = 0
max_div = 20
answer = False

while answer == False:
    number += max_div
    for divider in range(1, max_div + 1):
         if number % divider == 0:
            int_div += 1
            if int_div == max_div:
                answer = True
         else:
            int_div = 0
            break

print('Самым маленьким числом, которое делится нацело на все числа от 1 до ' + str(max_div) + ' является ' + str(number))