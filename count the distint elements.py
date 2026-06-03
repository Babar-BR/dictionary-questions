arr = [1,2,2,3,3,3,4]
seen={}
C=0
for i in arr:
    if i not in seen:
        C+=1
    seen[i] =1
print(C)


