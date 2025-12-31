# num = 1
# nums = [i for i in range(1,21)]
# while True:
#     if all(num % d == 0 for d in nums):
#         break
#     num += 1
# print(num)    

import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

nums = [i for i in range(1, 21)]

result = 1
for n in nums:
    result = lcm(result, n)


print(result)
