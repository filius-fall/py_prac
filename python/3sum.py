# nums = [3,3]
# target = 6


# def test():
#     h = {}
#     for i, num in enumerate(nums):
#         n = target - num
#         print(n,target,num)
#         if n not in h:
#             print(i)
#             h[num] = i
#             print(h[num])
#         else:
#             print("ESLE")
#             return [h[n], i]


# t = test()
# print(t)



nums = [-1,0,1,2,-1,-4]
k = []

# take index at num[i]

mid = len(nums)//2 - 1

for i,num in enumerate(nums):
    low = i+1
    high = len(nums) - 1
    while(low < high):
        print(nums[low],nums[high],nums[i])
        if nums[low] + nums[high] + nums[i] == 0:
            k.append(nums[low],nums[high],nums[i])
    
        low += 1
        high -=  1

print(k)