n1 = [1,2,3,4,5,6,7,8,9]

search_value = int(input())

def binary_sort(search_value):
    

    upper = len(n1) - 1
    lower = 0

    while lower < upper:
        half = int((upper + lower) / 2)
        
        half_value = n1[half]

        # print("search Value:",search_value)
        # print("Lower: ",upper)

        if search_value == half_value:
            return half_value
        elif search_value < half_value:
            upper = half_value - 1
        elif search_value > half_value:
            lower = half_value + 1

    # return None



k = binary_sort(search_value)

print(k)
