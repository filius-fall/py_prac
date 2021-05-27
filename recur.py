# def trec(a):
#     if len(a) == 1:
#         return len(a[0])
#     return len(a[0]) + trec(a[1:])


# k = trec(["ab", "c", "def", "ghij"])
# print(k)


# def ex(k):
#     if len(k) == 0:
#         return []
#     if k[0] % 2 == 0:
#         return [k[0]] + ex(k[1:])

#     else:
#         return ex(k[1:])

# a = ex([1, 2, 3, 4, 5])
# print(a)


# def triangle(s):
#     if s == 1:
#         return 1
#     elif s < 1:
#         return 0
#     else:
#         return s + triangle(s-1)

# a = triangle(int(input("Enter the number:")))
# print(a)


def find_x(a):
    if len(a) == 0:
        return 0

    if a[0] == 'x':
        return find_x(a[1:])
    else:
        return 1 + find_x(a[1:])


a = find_x('asdfghjklx')
print(a)