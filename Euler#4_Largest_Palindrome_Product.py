#Нахождение самого большого палиндрома, полученного умножением двух трехзначных чисел
Polindroms = []

for i1 in range(100, 1000):
    for i2 in range(100, 1000):
        mult_res = i1 * i2
        Mult_res = str(mult_res)
        if len(Mult_res) % 2 == 0:
            hn1 = Mult_res[0:3]
            hn2 = ''.join(reversed(Mult_res[3:6]))
            if hn1 == hn2:
                Polindroms.append(mult_res)

print('Число ' + str(max(Polindroms)) + ' является самым большим полиндромом, полученного умножением двух трехзначных чисел')