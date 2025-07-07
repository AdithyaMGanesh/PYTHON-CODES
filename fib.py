import sys
sys.setrecursionlimit(1000000)
F={0:0,1:1}
def fib(n):
    if n<=1:
        return(n)
    else:
        if n in F.keys():
            return (F[n])
        else:
            F[n] = fib(n-1) + fib(n-2)
            return(F[n])
print(fib(10000))