n=int(input("Enter a limit: "))
zcount=0
for i in range(1,n+1):
    j=str(i)
    if '0' in j:
        zcount+=j.count('0')
print(zcount)