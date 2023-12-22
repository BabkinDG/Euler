#Нахождение разности между суммой квадратов и квадратом суммы первых ста натуральных чисел
degree_of = 2
numbers = 100
sum_square = 0
square_sum = 0

for i in range(1, numbers+1):
    sum_square += i ** degree_of

for i in range(1, numbers+1):
    square_sum += i
square_sum = square_sum ** degree_of

difference = square_sum - sum_square

print('Разность между суммой квадратов и квадратом суммы первых ста натуральных чисел равна ' + str(difference))