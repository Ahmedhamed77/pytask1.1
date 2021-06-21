import math

def prime_factors(n):
    i = 2
    primeFactors=[]
    while i <= math.sqrt(n):
        while n % i == 0:
            primeFactors.append(i)
            n = n / i
        i = i + 1
    if n > 1 :
        primeFactors.append(n)
    return primeFactors

max_sum = 0
res_num = 0

for i in range(100,1000):
    currunt_sum = prime_factors(i)
    if len(currunt_sum) > 1:
        currunt_sum = sum(currunt_sum)
        if max_sum < currunt_sum:
            res_num = i
            max_sum = int(currunt_sum)
print(max_sum, res_num)