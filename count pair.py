a = [1, 1, 1, 2, 2, 3]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
count = 0
for i in d.values():
    count = count + i // 2
print("pairs", count)


