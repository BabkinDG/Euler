#10001-е простое число
P_Numbers = []
number = 1
prime_number = 10001

def IsPrime(n):
    if n % 2 == 0:
        return n == 2
    divider = 3
    while divider * divider <= n and n % divider != 0:
        divider += 2
    return divider * divider > n

while len(P_Numbers) < prime_number:
    number += 1
    if IsPrime(number) == True:
        P_Numbers.append(number)

print(str(prime_number) + '-м простым числом является ' + str(P_Numbers[prime_number-1]))