# a = 10
# b = 3
def div(a,b):
    i = -b
    print(i)
    j = 0
    count = 0
    while j < a/2:
        count += 1
        print(count)
        i += b
        print(i)
        if i > a:
            print('Inside count')
            return count
        
        j += 1



k = div(10,-3)
print(k)