arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
d = {}

for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
firstelement = secondelement = 0
firstfre = secondfre = -999
for k, i in d.items():
    if firstfre < i:
        secondfre = firstfre
        secondelement = firstelement
        firstfre = i
        firstelement = k
    elif firstfre != secondfre and i > secondfre:
        secondfre = i
        secondelement = k
print(secondfre, "and ", secondelement)

