def how_func(target,nubers):
    if target == 0: return []
    if target < 0: return None

    for i in nubers:
        rem = target - i
        returned_value = how_func(rem, nubers)
        if returned_value != None:
            returned_value.append(i)
            return returned_value
    return None

    


print(how_func(7, [5,3,4,7]))