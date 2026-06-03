arr = [1, 2, 3,2, 4,1]
seen={}
for i in arr:
    if i in seen:
        print(i)
        break

    seen[i] =1


