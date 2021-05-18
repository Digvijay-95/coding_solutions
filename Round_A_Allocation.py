def Solution(b,x):
    count=0
    x=sorted(x)
    while len(x):
        if b-x[0]>=0:
            b=b-x[0]
            count+=1
            del(x[0])
            print("Gone")
        else:
            break
    return count

i=int(input())
for d in range(i):
    n,b=map(int, input().split())
    x=list(map(int, input().split()))
    ans=Solution(b,x)
    print(f"Case #{d+1}: {ans}")