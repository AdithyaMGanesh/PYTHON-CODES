def longest(s,k):
    uc=0
    maxlen=0
    i=0
    j=1
    while( i<=j and i<len(s) and j<=len(s)):
        print(s[i:j])
        uc=len(set(s[i:j]))
        if(uc == k):
            maxlen=max(maxlen,len(s[i:j]))
            j+=1
        elif(uc<k):
            j+=1
        else:
            i+=1
    print(maxlen)
longest('aabacbebebe',3)