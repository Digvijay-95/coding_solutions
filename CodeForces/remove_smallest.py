def sm(prb):
    for _ in range(0,t):
        i=0
        while(i<len(prb[_][1])):
            j=i+1
            while(j<len(prb[_][1])):
                if(int(prb[_][1][j]-prb[_][1][i])<=1):
                    m=min(prb[_][1][j],prb[_][1][i])
                    if(m==prb[_][1][i]):
                        j+=1
                        prb[_][1].pop(i)
                        print(prb[_][1],i,j)
                        continue
                    if(m==prb[j]):
                        prb[_][1].pop(j)
                        continue

                j+=1
            i+=1
    if(len(prb[_][1])==0):
        print("YES!")
    else:
        print("NO!")      




t=int(input())
prb=[]
for i in range(0,t):
    prb.append(list())
    prb[i].append(int(input()))
    prb[i].append(list(map(int, input().split() )))
    i=0
    j=1
sm(prb)