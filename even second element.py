l = [12, 45, 78, 23, 90, 34, 56]
l1 = []  # even number list
for i in l:
    if i % 2 == 0:
        l1.append(i)
# -----------logic second largest--------------
first = second = third = -1
for i in l1:
    if first < i:
        third = second
        second = first
        first = i
    elif second != first and i > second:
        second = i
    elif third != second and i > third:
        third = i
print(first)
print(second)
print(third)




