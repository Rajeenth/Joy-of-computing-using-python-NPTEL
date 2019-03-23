

def isSymmetric(mat, N): 
    for i in range(N): 
        for j in range(N): 
            if (mat[i][j] != mat[j][i]): 
                return False
    return True
   

a = int(input())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isSymmetric(m, a)): 
    print("YES")
else: 
    print("NO")