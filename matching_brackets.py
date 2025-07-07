def isvalid(s):
    stack=[]
    for c in s:
        if c in '{([':
            stack.append(c)
        else:
            if (not stack or (c==']' and stack[-1]!='[')
             or (c=='}' and stack[-1]!='{') or
             (c==')' and stack[-1]!='(')):
                print("NOT MATCHING")
                exit(1)
            else:
                stack.pop()
    if len(s)==0:
        print("NOT MATCHING")
    else:
        print("MATCHING")
isvalid('{[(]}')       
