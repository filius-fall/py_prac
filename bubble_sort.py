# unoreder_list = [1,7,9,3,5,4,2,6]
# l = len(unoreder_list) - 1
# sorted = False

# while not sorted:
#     sorted = True
#     for i in range(l):
#         if unoreder_list[i] > unoreder_list[i+1]:
#             unoreder_list[i], unoreder_list[i+1] = unoreder_list[i+1],unoreder_list[i+1]
#             sorted = True
#     l -= 1
# print(unoreder_list)


def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        # unsorted_until_index -= 1
    return list


print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))