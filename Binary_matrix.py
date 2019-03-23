


def isBinaryMatrix(mat,M,N): 
    for i in range(M): 
        for j in range(N): 
            # Returns false if element 
            # is other than 0 or 1. 
            if ((mat[i][j] == 0 or mat[i][j] == 1)==False): 
                return False; 
  
    # Returns true if all the  
    # elements are either 0 or 1. 
    return True; 

a,b=map(int,input().split())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isBinaryMatrix(m,a,b)): 
    print("YES")
else: 
    print("NO")