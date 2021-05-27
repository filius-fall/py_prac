def test():
    s = "21474836406"
    k = ""
    l = []
    for i in s:
        print(i)
        try:
            if int(i):
                print('Inside Try')
                k = k + i
                # print(i)
                print(k)
        except:
            print('Inside Except')
            if i == "-" or i == "+":
                l.append(i)
                print('Detected -')
            elif i == " ":
                print("passing")
                pass
            else:
                print("I am breaking")
                break

    print(k)    
    if len(k) != 0:

        if len(l) > 1:
            return 0
        elif len(l) == 0:
            m = int(k)
        elif len(l) == 1:
            m = int(l[0] + k)
        if m > pow(-2,31) and m < pow(2,31)-1:
            print('With in pow')
            print(m)
        elif m < pow(-2,31):
            print('Low power')
            print(pow(-2,31))
        elif m > pow(2,31) - 1:
            print('High pow')
            print(pow(2,31) - 1)
    elif len(k) == 0:
        print(0)


test()