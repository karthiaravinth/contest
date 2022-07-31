for _ in range(1,1+int(input())):
	a = input()
	n = len(a)
	s = 0
	for i in range(n):
		s += int(a[i])
	v = 9-s%9
	i =0 
	if v==9:
		v = 0
		i = 1
	while i<n:
		if int(a[i]) > v:
			break
		i+=1
	print(f"Case #{_}:",a[:i]+str(v)+a[i:])