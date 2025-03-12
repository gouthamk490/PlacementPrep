n=int(input())
m=int(input())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
r,c=n-1,0
count=0
while r>=0 and c<m:
    if mat[r][c]<0:
        count+=1
        c+=1
    else:
        r-=1
        c=0
print(count)
