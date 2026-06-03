w = ["apple", "ant", "cat", "car", "dog"]
r={}
for i in w:
    f=i[0]
    if f not in r:
        r[f]=[]
    r[f].append(i)
print(r)