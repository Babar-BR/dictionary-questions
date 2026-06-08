a="abcabcd"
l=0
m=0
seen=set()
for r in range(len(a)):
    while a[r] in seen:
        seen.remove(a[l])
        l=l+1
    seen.add(a[r])
    m=max(m,r-l+1)
print(m)