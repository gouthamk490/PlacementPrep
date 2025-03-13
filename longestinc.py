n=int(input())
l=list(map(int,input().split()))
res=[]
current=[l[0]]
for i in range(1,n):
    if l[i]>l[i-1]:
        current.append(l[i])
    else:
        if len(current)>len(res):
            res=current
        current=[l[i]]
if len(current)>len(res):
    res=current
print(*res)
