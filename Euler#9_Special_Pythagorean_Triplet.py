import sys

for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a < b and b < c and (a + b + c == 1000) and (a**2 + b**2 == c**2):
                result = a*b*c
                print(f'{result} {a} {b} {c}')
                sys.exit()