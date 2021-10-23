a = [1,2,3,,0,0,0]
b = [4,5,6]
m = 3
n = 3
i = 0
j = 0

# for i in range(len(b)):
#     a.append(b[i])

k = []

while i<m and j<n:
    if b[j] <= a[i]:
        print('INS')
        a.insert(i-1,b[j])
        print(a)
        j = j+1
    else:
        i = i+1
print(a)
