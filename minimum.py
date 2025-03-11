stri = input()
tot = 0
avail = 0

for i in stri:
    if i in ['C', 'U']:
        if avail > 0: 
            avail -= 1
        else:
            tot += 1
    elif i in ['R', 'L']:
        avail += 1 
print(tot)
