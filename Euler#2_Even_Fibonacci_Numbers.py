#Сумма четных членов последовательности Фибоначи до 4 000 000
summ = 0
fnum = [1]
fnew = 0
range = 4000000

while fnew < range - 1:
    fnew = fnum[len(fnum) - 1] + fnum[len(fnum) - 2]
    if fnew < range:
        fnum.append(fnew)
    if (fnew % 2) == 0 and fnew < range:
        summ += fnew

print(fnum)
print(summ)
print('Сумма четных членов последовательности Фибоначи до 4 000 000 равна ' + str(summ))