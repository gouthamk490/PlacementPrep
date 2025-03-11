n=int(input())
count=n
sum=0
while(n!=0):
    x=float(input())
    sum+=x
    n-=1
print(f"The average is: {sum/count:.3f}")
