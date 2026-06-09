a = [1, 2, 3, 4]
s = 0
prefixsum = []
for i in range(len(a)):
    s = s + a[i]
    prefixsum.append(s)
print("Prefix Sum List:", prefixsum)
L = int(input("Enter starting index (L): "))
R = int(input("Enter ending index (R): "))


if L == 0:
    range_sum = prefixsum[R]
else:
    range_sum = prefixsum[R] - prefixsum[L - 1]

print(f"The sum from index {L} to {R} is: {range_sum}")
