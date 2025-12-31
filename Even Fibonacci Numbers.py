n = 4000000
a = 0 
b = 1
sum = 0
while b < n:
    a , b = b , a+b
    if a % 2 == 0:
        sum +=  a
print(sum)