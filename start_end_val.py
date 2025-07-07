
def query_val(n,query):
    a = [0]*(n+1)
    for st,en,val in query:
        a[st] += val
        a[en] -= val
    peak=0
    sum=0
    for i in a:
        sum+=i
        peak=max(peak,sum)
    print(peak)
query_val(10,[[1,5,3], [4,8,7], [6,9,1]])