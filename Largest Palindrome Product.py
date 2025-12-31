n = 999
x = 0
new = []
for i in range(100 , n):
    for j in range(i+1 , n):
        x = i * j
        if x == int(str(x)[::-1]):
            new.append(x)
new.sort()
print(new[-1])

