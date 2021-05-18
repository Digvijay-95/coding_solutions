mylist=[]
count=0
for _ in range(1,5):
	mylist.append(int(input()))
d=int(input())
x=min(mylist)
if x==1:
	print(d)
else:
	for i in range(1,d+1):
		if(i<x):
			count+=1
			i+=1
			continue
		elif i%mylist[0]!=0 and i%mylist[1]!=0 and i%mylist[2]!=0 and i%mylist[3]!=0:
			count+=1
			i+=1
			continue
	print(count)