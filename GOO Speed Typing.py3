for _ in range(1,1+int(input())):
	a = input()
	b = input()
	n = len(a)
	m = len(b)
	i =0 ;j =0
	if n>m:
		print(f"Case #{_}:","IMPOSSIBLE")
		continue
	elif n==m:
		k = True
		while (j<m):
			if a[i] == b[j]:
				i+=1
				j+=1
			else:
				k = False
				break
		if k:
			print(f"Case #{_}: 0")
		else:
			print(f"Case #{_}:","IMPOSSIBLE")
		continue
	else:
		while (j<m and i<n):
			if a[i] == b[j]:
				i+=1
				j+=1
			else:
				j+=1
		if i == n and j == n:
			print(f"Case #{_}:",m-n)
		elif i == n:
			print(f"Case #{_}:",m-i)
		else:
			print(f"Case #{_}:","IMPOSSIBLE")



