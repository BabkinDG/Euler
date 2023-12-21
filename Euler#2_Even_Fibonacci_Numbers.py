#Сумма четных членов последовательности Фибоначи до 4 000 000
summ = 0
F = [1]
Fnew = 0
range = 4000000

while Fnew < range - 1:
    Fnew = F[len(F)-1] + F[len(F)-2]
    if Fnew < range:
        F.append(Fnew)
    if (Fnew % 2) == 0 and Fnew < range:
        summ += Fnew

print(F)
print(summ)
print('Сумма четных членов последовательности Фибоначи до 4 000 000 равна ' + str(summ))