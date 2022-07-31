for _ in range(1,1+int(input())):
    n = int(input())
    s = input()
    low = 0
    high = 0
    num = 0
    spe = 0
    for k in s:
        if '0' <= k <= '9':
            num += 1
        if 'A' <= k <= 'Z':
            high+=1
        if 'a' <= k <= 'z':
            low+=1
        if (k=='#' or k == '@' or k=='*' or k=='&'):
            spe += 1 
    #print(num,spe,low,high)
    if num == 0:
        s+='1'
    if spe == 0:
        s+='*'
    if high == 0:
        s+='A'
    if low == 0:
        s+='f'
    if len(s)<7:
        j = len(s)
        s += (7-j)*'d'
    print(f'Case #'+str(_)+': '+s)
    
