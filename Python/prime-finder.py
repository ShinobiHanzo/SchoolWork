import math
prime_list = []
primeCount =0

def primeFinder(num):
    j = 2
    passCount = 0
    while passCount !=3:
        for i in range(num):
            if (num%(1+i))==0:
                passCount+=1
    if passCount <=2:
        prime_list.append(num)
        primeCount+=1
        return
    else:
        return

searchRangeMin = int(input("enter lowest value: "))
searchRangeMax = int(input("enter highest value: "))

for i in range(searchRangeMin, searchRangeMax):
    if i >= searchRangeMin and i<=searchRangeMax:
        primeFinder(i)
print ("\nThe number of primes between", str(searchRangeMin),
        "and",str(searchRangeMax), "have a total of", primeCount, "prime numbers")
print(prime_list)
