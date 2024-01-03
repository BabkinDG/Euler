#Нахождение самого большого палиндрома, полученного умножением двух трехзначных чисел
polindroms = []

for i1 in range(100, 1000):
    for i2 in range(100, 1000):
        mult_res = i1 * i2
        if str(mult_res)[0:3] == ''.join(reversed(str(mult_res)[3:6])):
            polindroms.append(mult_res)

max_pol = max(polindroms)
print(f'Число {max_pol} является самым большим полиндромом, полученного умножением двух трехзначных чисел')