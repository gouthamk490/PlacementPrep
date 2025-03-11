n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
s=0
for i in l:
    if i%2!=0:
        s+=1
if s:
    print(f"Odd Elements: {s}")
else:
    print("No odd elements are present")
