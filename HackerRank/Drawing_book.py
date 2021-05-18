#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if(p==0 or p==n or p==1):
        return 0
    else:
        if(n%2==0):
            max_turn=n/2
            
        else:
            max_turn=(n-1)/2
            
    if(p%2!=0):
        p=p-1

        #Max_turn is also mid of book
        
    if(p<=max_turn):
        return int(p/2);
    else:
        return int(max_turn-(p/2))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

