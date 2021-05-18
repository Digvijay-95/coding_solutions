def Rotation(param,a,b):
    #print(f"a={a}, b={b}")
    #print(param[4])
    for n in range(a-b,a):
        print(param[n],end=" ")
    for u in range(a-b):
        print(param[u],end=" ")

x=int(input())
for i in range(x):
    a,b=map(int, input().split(" "))
    param=list(map(int, input().split(" ")))
    if(b>a):
        b=b%a
    Rotation(param,a,b)