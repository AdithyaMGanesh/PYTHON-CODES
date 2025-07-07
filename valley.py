def valley(inp):
    sealevel = 0
    a=[]
    for i in inp:
        if i == 'U':
            sealevel += 1
        if i == 'D':
            sealevel -= 1
        if i == 'U' and sealevel==0:
            sealevel += 1
    print(sealevel)
valley('UUDDDDUDUU')