s1 = "listen"
s2 = "silent"
d={}
for i in s1:
    d[i]=d.get(i,0)+1
for i in s2:
    d[i]=d.get(i,0)-1
f=True
for i in d.values():
    if i!=0:
        f=False
if f:
    print("angram")
else:
    print("no")



