a = [5, 9, 1, 8]
an = []
m = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        l = []
        s = 0
        for k in range(i, j + 1):
            l.append(a[k])
            s = s + a[k]
        if len(l) == 3:
            m = max(m, s)
print(m)



