marks = {
    "math": 90,
    "science": 85,
    "english": 95,
    "social": 80
}
a=-1
b=""
for k,i in marks.items():
    if i>a:
        a=i
        b=k
print(b)