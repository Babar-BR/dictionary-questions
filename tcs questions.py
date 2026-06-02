def find(start_date, n):
    d = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}

    start = d[start_date]
    count = 0
    for day in range(1, n + 1):
        day_of_week = (start + day - 1) % 7  # only this
        if day_of_week == 6:
            count += 1
    return count


print(find("mon", 13))

n = len(bin(10)) - 2
mask = (1 << n) - 1
r = mask ^ 10
print(r)
