i = 2
primee = []

while len(primee) < 10001:
    
    for y in range(2 , int(i ** 0.5)+1):
        if i % y == 0:
            is_prime = False
            break     
    else :    
        primee.append(i)   
    i += 1                
print(primee[-1])    



