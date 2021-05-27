l = [1,2,4,2,3,4]
m = []
a = l

for i in range(0,len(l)-1):
    k = a.pop(0)
    print(k)
    if k not in a:
        m.append(k)

if a[0] not in m:
    m.append(a[0])
    print(m)