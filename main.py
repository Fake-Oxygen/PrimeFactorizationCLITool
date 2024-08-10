import sys

num = int(sys.argv[1])
prime_factors = []
div = 2

while num > 1:
    if num % div == 0:
        prime_factors.append(div)
        num = num / div
    else:
        div += 1
print(prime_factors)
