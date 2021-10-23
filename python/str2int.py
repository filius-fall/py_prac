def myAtoi(s):
        """
        :type str: str
        :rtype: int
        """

        if (len(s) == 0):
            return 0

        s = s.strip()
        try:
            if(s[0].isdigit()):
                sign = 1
            elif(s[0] == '+'):
                sign = 1
                s = s[1:]
            elif(s[0] == '-'):
                sign = -1
                s = s[1:]
            else:
                return 0
        except:
            return 0

        l = len(s)
        val = "";    i = 0
        while(i < l and s[i].isdigit()):
            val = val * 10 + eval(s[i])
            val += s[i]
            i += 1

        # val = int(val)
        val = sign * val

        if(val > 2147483647):
            return 2147483647
        elif(val < -2147483648):
            return -2147483648
        else:
            return val


k = myAtoi(" ")
print(k)