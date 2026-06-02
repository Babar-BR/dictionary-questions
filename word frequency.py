s = "python is good python is easy"

d={}
for i in s.split():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)