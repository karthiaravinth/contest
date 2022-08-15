d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
for _ in range(1,1+int(input())):
    s = input()
    f = input()
    l1 = len(s)
    l2 = len(f)
    c = 0
    for i in range(l1):
        m =30
        for j in range(l2):
            if s[i] == f[j]:
                m = 0
                
                break
            mx = min(abs(d[s[i]]-d[f[j]]),26 -abs(d[s[i]]-d[f[j]]))
            if mx < m:
                m = mx
        c += m
        #print(i,j,c)
    print("Case #{}: {}".format(_,c))