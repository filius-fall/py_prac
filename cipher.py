import string
#testing new ssh commit 111 222
def cipher(msg,shift,decrypt=False):
    lowercase = string.ascii_lowercase
    uppercase=string.ascii_uppercase
    result=""

    if decrypt:
        shift = shift*-1

    for ms in msg:
        if ms.islower():
            index=lowercase.index(ms)
            result+=lowercase[(index+shift)%26]
        else:
            index=uppercase.index(ms)
            result+=lowercase[(index+shift)%26]

    return result


k=cipher('sreeram',5)
print(k)