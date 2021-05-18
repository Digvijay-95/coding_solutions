x=input()
song=[]
sets=[]
for _ in range(x):
	m=0
	n=input()
	for __ in range(n):
		t=input()
		song.append(t)
	
	sets=list(set(song))
	
	for ___ in range(n):
		temp=song[___]+1
		if !(temp in sets):
			song[___]=temp
			m=m+1