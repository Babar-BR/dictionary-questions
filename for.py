def oddno(n):
    if n % 2 != 0:
        return n


l = [11, 22, 13, 40, 17, 50]

for i in l:
    r = oddno(i)
    if r!=None:
        l.append(i)
print(l)






