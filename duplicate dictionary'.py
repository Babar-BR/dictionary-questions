arr = [1,2,3,2,4,5,1,6]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=[]
for k,i in d.items():
    if i>1:
        l.append(k)
print(l)
