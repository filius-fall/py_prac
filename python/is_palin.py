s = "A man, a plan, a canal: Panama"
# s = "ab"
k = ""

for i in s:
    if i.isalnum():
        k += i.lower()

for i in range(len(k)):
    # l = -(i+1)
    if k[i] == k[int(-(i+1))]:
        print(i)
        pass
    else:
        print('Break')

print(k)