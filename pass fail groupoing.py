marks = {
    "Ram": 85,
    "Shyam": 45,
    "Ravi": 75,
    "Anu": 30
}

r = {
    "pass": [],
    "fail": []

}
for k, i in marks.items():
    if i > 50:
        r["pass"].append(k)
    else:
        r["fail"].append(k)
print(r)
