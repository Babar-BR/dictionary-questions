s = "abcbb"
seen = set()
left = 0
max_len = 0
start = 0

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    curr_len = right - left + 1

    if curr_len > max_len:
        max_len = curr_len
        start = left

print("Length:", max_len)
print("Substring:", s[start:start + max_len])