for _ in range(1,1+int(input())):
	r,c = map(int,input().strip().split(" "))
	print(f"Case #{_}:" )
	print(".."+'-'.join(['+' for i in range(c)]))
	print(".."+'.'.join(['|' for i in range(c)]))
	for i in range(((r-1)*2)+1):
		if i%2==0:
			print('-'.join(['+' for i in range(c+1)]))
		else:
			print('.'.join(['|' for i in range(c+1)]))
