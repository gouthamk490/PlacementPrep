n=int(input())
flag=1
for i in range(2,n//2+1):
    if n%i==0:
        flag=0
        break
if flag:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
