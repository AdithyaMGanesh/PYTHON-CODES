n=int(input())
primes=[2]
size=((n-3)//2) +1
isPrime=[True]*size

def markFalse(a,n):
    p=2*a+3
    for i in range(2*a**+6*a+3,size,p):
        isPrime[i]=False
for i in range(0,size):
    if isPrime[i]==True:
        primes.append(2*i+3)
        markFalse(i,n)
print(primes)
 