def markFalse(a,n):
    for i in range(a,n+1,a):
        isPrime[i]=False
 
n=int(input())
primes=[]
isPrime=[True]*(n+1)
isPrime[0]=False
isPrime[1]=False

primes.append(2)
markFalse(2,n)

for i in range(3,n+1,2):
    if isPrime[i]==True:
        primes.append(i)
        markFalse(i,n)
print(primes)


