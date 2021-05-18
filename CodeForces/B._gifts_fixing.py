def fix(problem,t):
    for i in range(0,t):
        
        a=min(problem[i][1])
        b=min(problem[i][2])
        p=0
        count=0
        if(problem[i][1].count(a)==len(problem[i][1]) and problem[i][2].count(b)==len(problem[i][2])):
            print(0)
            continue
        
        while(p<problem[i][0]):
            
            n=min( (problem[i][1][p] - a),problem[i][2][p]-b)
            
            if(problem[i][1][p]>a and problem[i][2][p]>b):
                problem[i][1][p]=(problem[i][1][p])-n
                
                problem[i][2][p]=(problem[i][2][p])-n
                
                count=count+(n)
                
                if(problem[i][1][p]>a):
                    
                    count=count+(problem[i][1][p])-a
                    
                    problem[i][1][p]=a
                    
                if(problem[i][2][p]>b):
                    
                    count=count+(problem[i][2][p]-b)
                    problem[i][2][p]=b
                    
                p+=1
                continue
            if(problem[i][1][p]>a):
                
                count=count+(problem[i][1][p]-a)
                problem[i][1][p]=a
                
                p+=1
                continue
            if(problem[i][2][p]>b):
                
                count=count+(problem[i][2][p]-b)
                
                problem[i][2][p]=b
                
                p+=1
                continue
            p+=1
        print(count)                
        
problem=[]
t=int(input())
for i in range(0,t):
    problem.append(list())
    problem[i].append(int(input()))
    problem[i].append(list(map(int,input().split())))
    problem[i].append(list(map(int,input().split())))
    print(problem)
fix(problem,t)