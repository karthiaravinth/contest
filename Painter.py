def fun(v,s,n):
    mi = 0
    ls = -3
    if v =='R':
        o1 = 'O'
        o2 = 'P'
    elif v =='B':
        o1 = 'G'
        o2 = 'P'  
    elif v =='Y':
        o1 = 'O'
        o2 = 'G' 
    for i in range(0,n):
        if s[i] =="U":
            continue
        if s[i]==v or s[i]=='A' or o1 == s[i] or o2 == s[i]:
            if ls != i-1:
                mi+=1
            ls = i
    return mi

for _ in range(1,1+int(input())):
    n = int(input())
    s = input()
    c = 0
    for i in ['R','B','Y']:
        c += fun(i,s,n)
        
    print("Case #{}: {}".format(_,c))