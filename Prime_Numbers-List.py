n = int(input("Please enter a number between 1 and 100: "))
primes = []
for a in range(2, n):
    isPrime = True
    for i in range(2, a):
        if a % i == 0:
          isPrime = False
    if isPrime:
        primes.append(a)
print(primes)