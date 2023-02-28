from math import *

n = factorial(26) / factorial(26 - 10)
n1 = factorial(21) / factorial(21 - 10)
n2 = factorial(21) / factorial(21 - 9) * 10 * 5
print(n - n1 - n2)