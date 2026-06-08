a="babar"
l=[]
ans=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        tem=""
        for k in range(i,j+1):
            tem=tem+a[k]
        ans.append(tem)
print(ans)