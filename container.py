s = [1,8,6,2,5,4,8,3,7]

area_values = []
for i in range(len(s)):
    for j in range(i+1,len(s)):
        area = abs(min(s[i],s[j]) * (i-j))
        area_values.append(area)


print(max(area_values))