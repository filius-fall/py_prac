l = 5
k = "1 2 3 4 5"
k = map(int,k.split(" "))
k = list(k)

num = 0
for i in k:
    num += i

print(num,len(k),num%len(k))

m = (num%len(k))+ 1

print(m)
