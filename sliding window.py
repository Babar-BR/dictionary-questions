a=[5,1,8,9]
l=0
m=0
temp=0
ans=0
for r in range(len(a)):
    temp=temp+a[r]
    if(r-l==3):
        temp-=a[l]
        l=l+1
    if(r-l+1==3):
        ans=max(ans,temp)
print(ans)
