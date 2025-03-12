l=list(map(int,input().split(",")))
min_price=float('inf')
max_pro=0
for i in l:
    min_price= min(min_price,i)
    max_pro=max(max_pro,i-min_price)
print(max_pro)
