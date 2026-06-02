s = "aabbcdde"

d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for k,i in d.items():
    if i==1:
        print(k)
        break
