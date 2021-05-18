'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import sys
sys.setrecursionlimit(15000000)
# Write your code here
solutions=[]
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)


def xvalue(n):
    lcm=1
    fn=0;
    for _ in range(1,n+1):
        fn=fn+_
        lcm = lcm*_/(gcd(lcm , _))

    return lcm , fn

i=int(input())
for s in range(i):
    n=int(input())
    if(n==1):
        print(1,1)
        continue
    x , fn =xvalue(n)
    print(int(fn))

