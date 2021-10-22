import math
from time import time, ctime

def lucas_lehmer_sequence(p):
    ll_sequence = [4]
    if p>2:
        for i in range(1, (p-1)):
            n_i = ((ll_sequence[i-1] ** 2 - 2) % ((2 ** p) - 1))
            ll_sequence.append(n_i)
    return(ll_sequence)

def isPrime(number):
    if number <= 1 or (number > 2 and number % 2 == 0):
        return(False)
    
    for factor in range(2, int(math.sqrt(number)) + 1):
        if number % factor == 0:
            return(False)
    return(True)

def ll_prime(p):
    if p == 2:
        return(True)
    elif lucas_lehmer_sequence(p)[-1] == 0:
        return(True)
    return(False)

count = 0

for i in range(10000):
    if isPrime(i):
        if ll_prime(i):
            print(str(i) + " :::: Found @ " + str(ctime(time())))
            count += 1
            

print("----")
print("Count: " + str(count))