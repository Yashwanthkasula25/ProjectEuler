n  = 600851475143
m = 2
while m * m <= n:
    if n%m == 0:
        n //= m
    else:
        m  += 1
print(n)         

