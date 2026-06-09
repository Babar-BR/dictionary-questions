a = [8, 4, 3, 2]
k = 4
s = 0
p = []
for i in range(len(a)):
    s = s + a[i]
    p.append(s)
print(p)
count = 0
for l in range(len(a)):
    for r in range(l, len(a)):
        if l == 0:
            csum = p[r]
        else:
            csum = p[r] - p[l - 1]
        if csum == k:
            count += 1
print(count)





