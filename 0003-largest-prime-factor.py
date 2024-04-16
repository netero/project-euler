# What is the largest prime factor of the number 600851475143

def isPrime(num):
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True

def largePrimeFactor(num):
    for i in range(2,num):
        if num%i == 0:
            divided = int(num / i)
            if isPrime(divided):
                return divided
            


print(largePrimeFactor(13195))
print(largePrimeFactor(600851475143))