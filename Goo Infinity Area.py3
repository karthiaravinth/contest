import math
for _ in range(1,1+int(input())):
	r,a,b = map(int,input().split())
	c = 0
	m = 0
	while (True):
		ex = r*r
		m += ex
		m += (ex*a*a)
		if r<=0:
			print("Case #"+str(_)+': '+str(round(m*math.pi,6)))
			break
		r = r*a//b
		c += 2