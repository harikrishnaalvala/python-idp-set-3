n=int(input())
mat=[]
for i in range(n):
    m=list(map(int,input().split()))
    mat.append(m)
s=0
for i in range(n):
    for j in range(n):
        if (i==j) or (i+j==n-1):
            s+=mat[i][j]
print(s)
