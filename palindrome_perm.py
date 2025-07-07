"""import itertools
s=input(())
new=set(itertools.permutations(s))
lis=[]
for i in new:
    m="".join(i)
    lis.append(m)
for i in lis:
    if i==i[-1::-1]:
       return True
return False"""

from collections import Counter
n = input("Enter a string : ")
counterDict = Counter(n)
oddCount = 0
for i in counterDict.values():
    if i%2==1:
        oddCount+=1
if oddCount>1:
    print("No")
else:
    print("Yes")
