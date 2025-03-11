l=list(map(int,input().split()))
mat1=[]
for i in range(l[0]):
    r=list(map(int,input().split()))
    mat1.append(r)
mat2=[]
for i in range(l[0]):
    r=list(map(int,input().split()))
    mat2.append(r)
print("First Matrix:")
for r in mat1:
    print(*r)
print("Second Matrix:")
for r in mat2:
    print(*r)
print("Sum of the two matrices is:")
result=[]
for i in range(l[0]):
    r=[]
    for j in range(l[1]):
        r.append(mat1[i][j]+mat2[i][j])
    result.append(r)
for r in result:
    print(*r)
