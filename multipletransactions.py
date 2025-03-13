l = list(map(int,input().split(',')))
max_profit=0
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        max_profit+=l[i]-l[i-1]
print(max_profit)
