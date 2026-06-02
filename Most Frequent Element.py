arr = [1,2,2,3,3,3,4]

d={}

for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
a=-100
print(d)
for k,i in d.items():
    if i>a:
        a=i
print(a)