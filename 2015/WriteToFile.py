f = open("out.txt",'w')
for x in range(1,5000):
	print("%d,%d,-1" %(x,x+1), file = f)
f.close()