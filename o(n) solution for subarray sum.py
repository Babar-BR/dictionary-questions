arr = [2, 1, 4, 3]
k = 5
d = {0: 1}
csum = 0
count = 0
for i in arr:
    csum += i
    need = csum - k
    if need in d:
        count = count + d[need]
    d[csum] = d.get(csum, 0) + 1
print(count)



