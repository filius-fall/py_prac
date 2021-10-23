nums = [2,2,1]

def single(n):

    for i in range(len(n)):
        print(n)
        k = n.pop(0)
        print(n)
        print(k)

        if k in n:
            print('In pass')
            n.remove(k)
            pass
        else:
            return k
        
        if len(n) == 1:
            print('INSSDE')
            print(n)
            return n[0]
l = single(nums)
print(l)