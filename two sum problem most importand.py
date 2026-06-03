a=[1,8,3,6,5,4,7,1,2]
target=9
seen={}
for i in range(len(a)):
    n=a[i]
    need=target-n
    if need in seen:
        print([seen[need],i])
    seen[n]=i
