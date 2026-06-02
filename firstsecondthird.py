l = [33, 25, 56, 78]
# print(sorted(l))
# largest=-1
# for i in l:
#     if largest<i:
#         largest=i
# print("largest element",largest)

# first=second=third=-1
# for i in l:
#     if first<i:
#         second=first
#         first=i
#     elif second!=first and i>second:
#         second=i
# print(second)
first = second = third = -1
for i in l:
    if i > first:
        third = second
        second = first
        first = i
    elif second != first and i > second:
        third = second
        second = i
    elif third != second and i > third:
        third = i
print(third)
print(second)


