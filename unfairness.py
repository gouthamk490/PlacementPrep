l=list(map(int,input().split(',')))
l=sorted(l)
n=int(input())
min_unfairness=float('inf')
res=[]
for i in range(len(l)-n+1):
    arr=l[i:i+n]
    unfairness=max(arr)-min(arr)
    if unfairness<min_unfairness:
        min_unfairness=unfairness
        res=arr
print(*res)
