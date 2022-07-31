import math
def pal(s):
    return s==s[::-1]
for _  in range(1,1+int(input())):
    c = 1
    n = int(input())
    sn = math.sqrt(n)
    if n ==1:
        print(f'Case #'+str(_)+': 1')
        continue
    elif n==2:
        print(f'Case #'+str(_)+': 2')
        continue
    elif n ==3:
        print(f'Case #'+str(_)+': 2')
        continue
    elif n==4:
        print(f'Case #'+str(_)+': 3')
        continue
    if pal(str(n)):
        c+=1
    if sn//1 == sn:
        if pal(str(int(sn))):
            c+=1
    for i in range(2,math.ceil(sn)):
        if n%i==0:
            if pal(str(i)):
                c+=1
            if pal(str(int(n/i))):
                c+=1
    print(f'Case #'+str(_)+': '+str(c))