#Сумма четных членов последовательности Фибоначи до 4 000 000
summ = 0
Fnum = [1]
Fnew = 0
range = 4000000

while Fnew < range - 1:
    Fnew = Fnum[len(Fnum) - 1] + Fnum[len(Fnum) - 2]
    if Fnew < range:
        Fnum.append(Fnew)
    if (Fnew % 2) == 0 and Fnew < range:
        summ += Fnew

print(Fnum)
print(summ)
print('Сумма четных членов последовательности Фибоначи до 4 000 000 равна ' + str(summ))