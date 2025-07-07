arr= [12,11,13,9,12,8,14,13,15]
n=len(arr)
out1=[0]
out2=[0]
out3=[0]
minsf=arr[0]
maxsf=0
for i in arr:
    minsf=min(minsf,i)
    out1.append(max(i-minsf,out1[-1]))
for i in range(n-1,-1,-1):
    maxsf=max(maxsf,arr[i])
    out2.insert(0,maxsf-arr[i])
for i in range(0,n):
    out3.append(out1[i]+out2[i])
new=list(set(out3))
new.sort()
print(new[-1])