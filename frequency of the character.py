    a = "babar"
s = ""
for i in range(len(a)):
    if a[i] not in s:
        count = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                count += 1
                s += a[i]
        print(a[i], count)
