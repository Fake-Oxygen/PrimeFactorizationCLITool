import sys
from collections import Counter

try:
    num = int(sys.argv[1])
except:
    sys.exit("Enter a number as an argument")

prime_factors = []
div = 2

while num > 1:
    if num % div == 0:
        prime_factors.append(div)
        num = num / div
    else:
        div += 1

exp_prime_factors = Counter(prime_factors)

print(prime_factors)

for key in exp_prime_factors.keys():
    print(key, "^", exp_prime_factors[key])
