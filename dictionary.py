# d1={"name":"Babar","age":20,"city":"Hyderabad"}
# for i in d1.values():
#     print(i)
d2={"math":90,"science":80,"english":70}
for k,i in d2.items():
    if i>75:
        print(k)
# d3={"a":10,"b":20,"c":30}
# sum1=0
# for i in d3.values():
#     sum1=sum1+i
# print(sum1)
# d4={"x":100,"y":200}
# print(d4.get("z"))
d5={"a":1,"b":2,"c":3}
for k,i in d5.items():
    d5[k]=i*2
print(d5)


d1= {"math":90,"science":80,"english":70,"social":95}
for k,i in d1.items():
    if i>=90:
        print(k)