def st(b):
	a = []
	for i in b:
		a.append(i)
	k = [0,0,0,0]
	kind = [0,0,0,0]
	mn = a[3]
	mnind = 3
	for i in range(3):
		if a[i]<mn:
			mn  =a[i]
			mnind = i
	a[mnind] = 99999999
	k[0] = mn
	kind[0] = mnind
	mn = a[3]
	mnind = 3
	for i in range(3):
		if a[i]<mn:
			mn  =a[i]
			mnind = i
	a[mnind] = 99999999
	k[1] = mn
	kind[1] = mnind		
	mn = a[3]
	mnind = 3
	for i in range(3):
		if a[i]<mn:
			mn  =a[i]
			mnind = i
	a[mnind] = 99999999
	k[2] = mn
	kind[2] = mnind
	k[3] = a[6-sum(kind)]
	kind[3] = 6-sum(kind)
	return k,kind

for _ in range(1,1+int(input())):
	a = list(map(int,input().strip().split(" ")))
	b = list(map(int,input().strip().split(" ")))
	c = list(map(int,input().strip().split(" ")))
	print(f"Case #{_}:" ,end=" ")
	if max(a+b+c)>1000000:
		print("IMPOSSIBLE")
		continue
	min1 = min(a[0],b[0],c[0])
	min2 = min(a[1],b[1],c[1])
	min3 = min(a[2],b[2],c[2])
	min4 = min(a[3],b[3],c[3])
	mn = [min1,min2,min3,min4]
	if 1000000 > min1+min2+min3+min4:
		print("IMPOSSIBLE")
	elif 1000000 == min1+min2+min3+min4:
		print(f"{min1} {min2} {min3} {min4}")
	else:
		su = 0 
		minval,minvalind = st(mn)
		mx = minval[-1]
		if mx == 1000000:
			for i in range(4):
				if i ==	minvalind[-1]:
					print(mn[i],end=" ")
				else:
					print(0,end=" ")
			print()
			continue
		elif mx > 1000000:
			print("IMPOSSIBLE")
			continue
		su = mx+minval[0]
		if su == 1000000:
			for i in range(4):
				if i ==	minvalind[-1] or i ==minvalind[0]:
					print(mn[i],end=" ")
				else:
					print(0,end=" ")
			print()
			continue
		elif su > 1000000:
			sec = 1000000-mx
			for i in range(4):
				if i ==	minvalind[-1]:
					print(mn[i],end=" ")
				elif i ==minvalind[0]:
					print(sec,end=" ")
				else:
					print(0,end=" ")
			print()
			continue
		else:
			su = mx+minval[0]+minval[1]
		if su == 1000000:
			for i in range(4):
				if i ==	minvalind[-1] or i==minvalind[0] or i==minvalind[1]:
					print(mn[i],end=" ")
				else:
					print(0,end=" ")
			print()
			continue
		elif su > 1000000:
			sec = 1000000-(mx+minval[0])
			for i in range(4):
				if i ==	minvalind[-1] or i==minvalind[0]:
					print(mn[i],end=" ")
				elif i ==minvalind[1]:
					print(sec,end=" ")
				else:
					print(0,end=" ")
			print()
			continue
		else:
			su = mx+minval[0]+minval[1]+minval[2]
		if su == 1000000:
			for i in range(4):
				print(mn[i],end=" ")
			print()
			continue
		elif su > 1000000:
			sec = 1000000-(mx+minval[0]+minval[1])
			mn[minvalind[2]] = sec
			for i in range(4):
				print(mn[i],end=" ")
			print()
			continue
		else:
			print("IMPOSSIBLE")
