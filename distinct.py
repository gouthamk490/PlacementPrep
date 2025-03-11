n=int(input())
l=list(map(int,input().split()))
s=set(l)
if len(l)==len(s):
    print('false')
else:
    print('true')
